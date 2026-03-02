"""DLT pipeline for loading paginated NYC taxi trip data from the Zoomcamp API."""

import dlt
from dlt.sources.rest_api import rest_api_resources
from dlt.sources.rest_api.typing import RESTAPIConfig


@dlt.source
def taxi_rest_api_source():
    """Define dlt resources for the NYC taxi API."""
    config: RESTAPIConfig = {
        "client": {
            "base_url": (
                "https://us-central1-dlthub-analytics.cloudfunctions.net/"
                "data_engineering_zoomcamp_api"
            ),
        },
        "resource_defaults": {
            "write_disposition": "replace",
        },
        "resources": [
            {
            "name": "nyc_taxi_trips",
            "endpoint": {
                "path": "",
                "data_selector": "$",  # <-- clave: la respuesta ES la lista
                "paginator": {
                "type": "page_number",
                "page_param": "page",
                "base_page": 1,
                "stop_after_empty_page": True,
                "total_path": None,   # <-- clave: no existe "total" en el response
                },
            },
            }
        ],
    }

    yield from rest_api_resources(config)


pipeline = dlt.pipeline(
    pipeline_name="taxi_pipeline",
    destination="duckdb",
    dev_mode=True,
    refresh="drop_sources",
    progress="log",
)


if __name__ == "__main__":
    load_info = pipeline.run(taxi_rest_api_source())
    print(load_info)  # noqa: T201
