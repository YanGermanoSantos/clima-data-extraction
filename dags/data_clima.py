from airflow.models import DAG, Variable
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.macros import ds_add
import pandas as pd
import pendulum
import os

# Caminho base dentro do container do Astro
BASE_PATH = "/usr/local/airflow/include"

with DAG(
    dag_id='dados_clima',
    start_date=pendulum.datetime(2026, 1, 23, tz="UTC"),
    schedule='0 0 * * 1', 
    catchup=False
) as dag:

    tarefa_1 = BashOperator(
        task_id = 'cria_pasta',
        bash_command = f'mkdir -p "{BASE_PATH}/semana={{{{ds}}}}"'
    )

    def extrai_dados(ds):
        city = 'Boston'
        key = Variable.get("visual_crossing_key")
        

        data_inicio = pendulum.parse(ds)
        data_fim = data_inicio.add(days=7).to_date_string()

        URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{ds}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv"
        
        dados = pd.read_csv(URL)

        file_path = f'{BASE_PATH}/semana={ds}/'

        dados.to_csv(file_path + 'dados_brutos.csv', index=False)
        dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv', index=False)
        dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv', index=False)

    tarefa_2 = PythonOperator(
        task_id = 'extrai_dados',
        python_callable = extrai_dados,
        op_kwargs = {'ds': '{{ds}}'} 
    )

    tarefa_1 >> tarefa_2