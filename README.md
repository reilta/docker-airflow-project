# docker-airflow-project
Trabalho final apresentado na disciplina DCA0132 - Engenharia de Dados, com o intuito de agendar, monitorar e orquestar tarefas em fluxo de dados (pipelines). Foi utilizado um dos datasets (voos2.csv) disponibilizados na [página do professor](https://www.dca.ufrn.br/~viegas/disciplinas/DCA0132/files/Datasets/).

### Instalação
```
git clone https://github.com/reilta/docker-airflow-project.git
```
### Exercutando
```
   docker-compose up airflow-init
   docker compose up
```
### Visualizando os serviços
```
  watch docker ps
```

### Visualizando o airflow

```
localhost:8080
```

### Parando e removendo os containers dos serviços
```
  docker compose down
```

### Conjunto de dados
Um dataset com informações sobre voos, contendo informações de voos internacionais, nacionais e regionais.

### Resultados obtidos
Carregamento e tranformação dos dados, tarefas para definir a quantidade e quais os países de origem dos voos, e também para os de destino; tarefa também para descobrir a quantidade de voos por cartegoria (nacional, internacional, regional) etc.
