from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


DBT_PROJECT_DIR = "/home/airflow/gcs/dags/dbt_machine_project/dbt"
DBT_PROFILES_DIR = "/home/airflow/gcs/dags/dbt_machine_project/dbt/profiles"


with DAG(
    dag_id="machine_master_dbt_dag",
    description="Run dbt transformation and data quality tests for machine master",
    start_date=datetime(2026, 8, 16),
    schedule="0 2 * * *",
    catchup=False,
    tags=["dbt", "bigquery", "machine-master"],
) as dag:

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"""
        set -e

        echo "Checking dbt project directory..."
        ls -la {DBT_PROJECT_DIR}

        echo "Checking dbt project file..."
        ls -la {DBT_PROJECT_DIR}/dbt_project.yml

        echo "Running dbt..."
        dbt run \
          --project-dir {DBT_PROJECT_DIR} \
          --profiles-dir {DBT_PROFILES_DIR}
        """,
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"""
        set -e

        echo "Running dbt tests..."

        dbt test \
          --project-dir {DBT_PROJECT_DIR} \
          --profiles-dir {DBT_PROFILES_DIR}
        """,
    )

    dbt_run >> dbt_test