"""@bruin
name: ingestion.trips
type: python
image: python:3.11
connection: duckdb-default

depends:
  - ingestion.payment_lookup

materialization:
  type: table
  strategy: append

columns:
  - name: pickup_datetime
    type: timestamp
    description: "When the meter was engaged"
  - name: dropoff_datetime
    type: timestamp
    description: "When the meter was disengaged"
@bruin"""

import os
import json
import pandas as pd


def materialize():
    start_date = os.environ["BRUIN_START_DATE"]
    end_date = os.environ["BRUIN_END_DATE"]
    bruin_vars = json.loads(os.environ.get("BRUIN_VARS", "{}"))
    taxi_types = [
        value.strip().lower()
        for value in bruin_vars.get("taxi_types", ["yellow"])
        if isinstance(value, str) and value.strip()
    ] or ["yellow"]

    start_ts = pd.Timestamp(start_date)
    end_ts = pd.Timestamp(end_date)

    month_starts = pd.date_range(
        start=start_ts.to_period("M").to_timestamp(),
        end=(end_ts - pd.Timedelta(microseconds=1)).to_period("M").to_timestamp(),
        freq="MS",
    )

    datetime_columns = {
        "yellow": ("tpep_pickup_datetime", "tpep_dropoff_datetime"),
        "green": ("lpep_pickup_datetime", "lpep_dropoff_datetime"),
        "fhv": ("pickup_datetime", "dropOff_datetime"),
        "fhvhv": ("pickup_datetime", "dropoff_datetime"),
    }

    location_payment_columns = {
        "yellow": ("PULocationID", "DOLocationID", "payment_type", "fare_amount"),
        "green": ("PULocationID", "DOLocationID", "payment_type", "fare_amount"),
    }

    frames = []
    for taxi_type in taxi_types:
        pickup_col, dropoff_col = datetime_columns.get(
            taxi_type, ("pickup_datetime", "dropoff_datetime")
        )

        for month_start in month_starts:
            url = (
                "https://d37ci6vzurychx.cloudfront.net/trip-data/"
                f"{taxi_type}_tripdata_{month_start:%Y-%m}.parquet"
            )
            
            extra_cols = location_payment_columns.get(
                taxi_type, ("PULocationID", "DOLocationID", "payment_type", "fare_amount")
            )

            cols_to_read = [pickup_col, dropoff_col, *extra_cols]

            try:
                dataframe = pd.read_parquet(url, columns=cols_to_read)
            except Exception as exc:
                print(f"Skipping {url}: {exc}")
                continue

            dataframe = dataframe.rename(
                columns={
                    pickup_col: "pickup_datetime",
                    dropoff_col: "dropoff_datetime",
                    "PULocationID": "pickup_location_id",
                    "DOLocationID": "dropoff_location_id",
                    "payment_type": "payment_type",
                    "fare_amount": "fare_amount",
                }
            )

            dataframe["taxi_type"] = taxi_type
            frames.append(dataframe)

    if not frames:
        return pd.DataFrame(
            columns=[
                "pickup_datetime",
                "dropoff_datetime",
                "pickup_location_id",
                "dropoff_location_id",
                "fare_amount",
                "taxi_type",
                "payment_type",
            ]
        )

    final_dataframe = pd.concat(frames, ignore_index=True)
    mask = (final_dataframe["pickup_datetime"] >= start_ts) & (
        final_dataframe["pickup_datetime"] < end_ts
    )
    return final_dataframe.loc[mask].reset_index(drop=True)