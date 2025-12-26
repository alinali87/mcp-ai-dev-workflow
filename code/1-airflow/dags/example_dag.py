"""
Example DAG demonstrating basic Airflow functionality
"""

from datetime import datetime, timedelta

from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG

# Default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


# Python callable function
def print_hello():
    """Print hello message"""
    print("Hello from Airflow!")
    return "Hello task completed"


def print_date():
    """Print current date"""
    print(f"Current date: {datetime.now()}")
    return "Date task completed"


# Define the DAG
with DAG(
    "example_basic_dag",
    default_args=default_args,
    description="A simple example DAG",
    schedule=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["example", "tutorial"],
) as dag:
    # Task 1: Print hello using Python
    hello_task = PythonOperator(
        task_id="print_hello",
        python_callable=print_hello,
    )

    # Task 2: Print date using Python
    date_task = PythonOperator(
        task_id="print_date",
        python_callable=print_date,
    )

    # Task 3: Echo using Bash
    bash_task = BashOperator(
        task_id="bash_echo",
        bash_command='echo "Running Bash task at $(date)"',
    )

    # Task 4: Sleep using Bash
    sleep_task = BashOperator(
        task_id="sleep_task",
        bash_command='sleep 2 && echo "Sleep completed"',
    )

    # Define task dependencies
    # hello_task runs first, then date_task and bash_task in parallel,
    # finally sleep_task runs after both complete
    hello_task >> [date_task, bash_task] >> sleep_task
