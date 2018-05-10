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

### Links:
- http://incubator-airflow.readthedocs.io/en/latest/installation.html
- http://airflow.apache.org/installation.html
- http://0.0.0.0:8080/admin/

### Reference Links:
- https://speakerdeck.com/artwr/apache-airflow-at-airbnb-introduction-and-lessons-learned
- https://www.agari.com/airflow-agari/
- https://hirelofty.com/blog/building-data-pipelines-python-part-one/
- http://site.clairvoyantsoft.com/installing-and-configuring-apache-airflow/
- http://site.clairvoyantsoft.com/setting-apache-airflow-cluster/
- http://site.clairvoyantsoft.com/making-apache-airflow-highly-available/
- https://www.slideshare.net/PyData/how-i-learned-to-time-travel-or-data-pipelining-and-scheduling-with-airflow-67650418
