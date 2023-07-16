# Departamento de Engenharia de Computação e Automação
# DCA0132 - Engenharia de Dados
# Trabalho Final - Projeto com Docker e Apache Airflow
# Discente: Reilta Christine Dantas Maia

from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

from datetime import datetime, timedelta
from statistics import mode

import pandas as pd
import os

# get dag directory path
dag_path = os.getcwd()

# initializing the default arguments that we'll pass to the DAG
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(5)
}

def transform_data():
    voos = pd.read_csv(f"{dag_path}/raw_data/voos2.csv", encoding="ISO-8859-1")

    data = voos
    data = data.drop('LongDest', 1)
    data = data.drop('LatDest', 1)
    data = data.drop('LongOrig', 1)
    data = data.drop('LatOrig', 1)

    data.to_csv(f"{dag_path}/dags/processed_data.csv", index=False)

def paises_destino():
    records = pd.read_csv(f"{dag_path}/dags/processed_data.csv", encoding="ISO-8859-1")

    print("quantidade de países de destino: ", records['Pais.Destino'].nunique())
    print("países de destino: ")
    print(records['Pais.Destino'].unique().tolist())

def paises_origem():
    records = pd.read_csv(f"{dag_path}/dags/processed_data.csv", encoding="ISO-8859-1")

    print("quantidade de países de origem: ", records['Pais.Origem'].nunique())
    print("países de origem: ")
    print(records['Pais.Origem'].unique().tolist())

def voo():
    records = pd.read_csv(f"{dag_path}/dags/processed_data.csv", encoding="ISO-8859-1")

    tipo = mode(records['Codigo.Tipo.Linha'])
    print(records['Codigo.Tipo.Linha'].value_counts())
    print("o tipo eh: ",tipo)
    return tipo


def tipo_voo(ti):
    tipo = ti.xcom_pull(task_ids = 'tipo')
    if (tipo == 'Internacional'):
        return 'internacional'
    elif (tipo == 'Nacional'):
        return 'nacional'
    else:
        return 'regional'

with DAG("voos", default_args=default_args,
         description='Aggregates the data for data analysis',
         schedule_interval = timedelta(days=1),catchup =False) as dag:
    
    task1 = PythonOperator(
        task_id = 'transform_data',
        python_callable = transform_data
    )

    task2 = PythonOperator(
        task_id = 'paises_destino',
        python_callable = paises_destino
    )

    task3 = PythonOperator(
        task_id = 'paises_origem',
        python_callable = paises_origem
    )

    task4 = PythonOperator(
        task_id = 'tipo',
        python_callable = voo
    )

    task5 = BranchPythonOperator(
        task_id = 'tipo_voo',
        python_callable = tipo_voo
    )

    internacional = BashOperator(
        task_id = 'internacional',
        bash_command = "echo 'Maior quantidade de voos internacionais!'"
    )

    nacional = BashOperator(
        task_id = 'nacional',
        bash_command = "echo 'Maior quantidade de voos nacionais'"
    )

    regional = BashOperator(
        task_id = 'regional',
        bash_command = "echo 'Maior quantidade de voos regionais'"
    )

    task1 >> [task2, task3] >> task4 >> task5 >> [internacional, nacional, regional]