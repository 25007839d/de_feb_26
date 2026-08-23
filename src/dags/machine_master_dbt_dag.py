from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


# dbt project is inside Airflow dags folder
DBT_PROJECT_DIR = "/opt/airflow/dags/dbt_machine_project"
DBT_PROFILES_DIR = "/opt/airflow/dags/dbt_machine_project"


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
        cd {DBT_PROJECT_DIR}

        dbt run \
          --project-dir {DBT_PROJECT_DIR} \
          --profiles-dir {DBT_PROFILES_DIR}
        """,
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"""
        cd {DBT_PROJECT_DIR}

        dbt test \
          --project-dir {DBT_PROJECT_DIR} \
          --profiles-dir {DBT_PROFILES_DIR}
        """,
    )

    dbt_run >> dbt_test