## Notes: 


### Installation of Airflow:

- pip install apache-airflow
- pip install apache-airflow[all]

### Initials:

- Change path for DAGs in ~/airflow/airflow.cfg
- Run airflow script : python <whatever-path>/<filename>.py

### Commands to test and validate:

- airflow list_dags
- airflow list_tasks <dag_id>
- airflow list_tasks <dag_id> --tree
- airflow test <dag_id> <task_id> 2015-06-01
- airflow backfill <dag_id> -s <start_date> -e <end_date>

### To run the local server:

- airflow webserver
