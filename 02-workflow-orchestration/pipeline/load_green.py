import pandas as pd
from sqlalchemy import create_engine

PARQUET_PATH = "../data/green_tripdata_2025-11.parquet"
engine = create_engine("postgresql+psycopg://root:root@localhost:5432/ny_taxi")

df = pd.read_parquet(PARQUET_PATH)
df.columns = [c.lower() for c in df.columns]

df.to_sql("green_tripdata_2025_11", engine, if_exists="replace", index=False)
print("Loaded rows:", len(df))
print("Columns:", list(df.columns))
