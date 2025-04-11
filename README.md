# docker-airflow-project
Final work presented in the course DCA0132 - Data Engineering, with the aim of scheduling, monitoring and orchestrating tasks in data flows (pipelines). One of the datasets (voos2.csv) available on [the teacher's page](https://www.dca.ufrn.br/~viegas/disciplinas/DCA0132/files/Datasets/) was used.

### Setup
```
git clone https://github.com/reilta/docker-airflow-project.git
```
### Running
```
   docker-compose up airflow-init
   docker compose up
```
### Viewing services
```
  watch docker ps
```

### Visualizing the airflow

```
localhost:8080
```

### Stopping and removing service containers
```
  docker compose down
```

### Data set
A dataset with flight information, containing information on international, national and regional flights.

### Results
Loading and transforming the data, tasks to define the number and countries of origin of the flights, and also for those of destination; task also to find out the number of flights by category (national, international, regional) etc.
