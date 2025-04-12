from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("✅ Hello from Airflow! Everything is working.")

default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    dag_id='simple_test_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=["test"],
) as dag:

    hello_task = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello,
    )

    hello_task
