from airflow.decorators import DAG, task
import pendulum
from airflow.operators.python import PythonOperator
import os

DAG_ID = "wikipedia_company_views"

with DAG(
    dag_id="wikipedia_company_views",
    start_date=pendulum.datetime(2025, 12, 26),
    schedule=None,
    catchup=False
) as dag:
    ...