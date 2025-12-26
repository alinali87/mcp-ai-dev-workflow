# Airflow Example

Apache Airflow 3.x example DAG with updated imports.

## DAG: example_basic_dag

A simple DAG demonstrating:
- Python operators
- Bash operators
- Task dependencies

## Key Changes for Airflow 3.x

Updated imports:
- `DAG` from `airflow.sdk`
- `BashOperator` from `airflow.providers.standard.operators.bash`
- `PythonOperator` from `airflow.providers.standard.operators.python`

## Tasks

1. `print_hello` - Python task that prints a hello message
2. `print_date` - Python task that prints the current date
3. `bash_echo` - Bash task that echoes with timestamp
4. `sleep_task` - Bash task that sleeps for 2 seconds

## Dependencies

```
hello_task → [date_task, bash_task] → sleep_task
```
