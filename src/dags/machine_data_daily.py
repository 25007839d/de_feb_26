from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.operators.dataproc import DataprocSubmitJobOperator
from datetime import datetime

from google.cloud import storage

from airflow.operators.empty import EmptyOperator

PROJECT_ID = "project-7792d7ca-4ff6-4f52-91b"
REGION = "asia-south1"
CLUSTER_NAME = "iot-demo-cluster"

with DAG(
    dag_id="machine_data_daily",
    start_date=datetime(2026, 8, 1),
    schedule= "5 */1 * * *",
    catchup=False,
) as dag:

    start = EmptyOperator(
        task_id="start"
    )

    spark_job = DataprocSubmitJobOperator(
        task_id="csv_to_bronze_machine_data_daily",
        project_id=PROJECT_ID,
        region=REGION,
        job = {
            "placement" : {
                "cluster_name" : CLUSTER_NAME,
            },
            "pyspark_job": {
                "main_python_file_uri": "gs://iot-data-lake-dk/spark_script/csv_to_bronze_machine.py"
            }
        }
    )
    end = EmptyOperator(
        task_id="end")

    start >> spark_job>> end