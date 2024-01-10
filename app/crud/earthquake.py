from datetime import datetime
from typing import Dict, List

from fastapi.responses import JSONResponse
from google.cloud import bigquery
from sqlalchemy.orm import Session

from app.schemas.earthquake import EarthquakeModel

project_id = "technical-test-env-408214"

client = bigquery.Client(project=project_id)

dataset_id = "test_alican"
table_id = "alican"


def get_earthquake(earthquake_id: int) -> Dict[str, str]:
    query = f"SELECT * FROM `{project_id}.{dataset_id}.{table_id}` WHERE earthquake_id = @earthquake_id"
    query_params = [
        bigquery.ScalarQueryParameter("earthquake_id", "INT64", earthquake_id)
    ]
    job_config = bigquery.QueryJobConfig(query_parameters=query_params)
    query_job = client.query(query, job_config=job_config)
    results = query_job.result()
    return results


def get_earthquakes(limit: int) -> List[Dict[str, str]]:
    if limit is None:
        limit = 500

    query = f"SELECT * FROM `{project_id}.{dataset_id}.{table_id}` LIMIT {limit}"
    query_job = client.query(query)
    results = query_job.result()
    return results


def create_earthquake(earthquake: EarthquakeModel) -> None:
    earthquake_dict = earthquake.dict()
    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)
    hello = client.insert_rows_json(table, [earthquake_dict])
    print("hello")
