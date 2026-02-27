# 🌦️ Airflow Weather Data Pipeline

Este projeto demonstra um pipeline de dados automatizado desenvolvido com **Apache Airflow** e **Astro CLI**. O objetivo é extrair dados meteorológicos históricos da cidade de Boston via API **Visual Crossing**, processar as informações e organizá-las em camadas para facilitar o consumo.

## 🚀 Tecnologias Utilizadas
* **Apache Airflow**: Orquestração e agendamento do pipeline.
* **Astro CLI**: Gerenciamento do ambiente via containers Docker.
* **Python**: Linguagem principal para extração e lógica de negócio.
* **Pandas**: Manipulação, limpeza e particionamento dos dados.
* **API Visual Crossing**: Fonte de dados climáticos via REST API.

## 🏗️ Arquitetura da DAG
O fluxo foi desenhado para ser resiliente e organizado:
1.  **`cria_pasta`**: Um `BashOperator` que cria diretórios dinâmicos na pasta `/include` do projeto, utilizando a macro `{{ds}}` para organizar os dados por data de execução.
2.  **`extrai_dados`**: Um `PythonOperator` que:
    * Consome a API utilizando chaves de segurança.
    * Calcula o intervalo de 7 dias dinamicamente com a biblioteca **Pendulum**.
    * Salva o dataset completo (`dados_brutos.csv`).
    * Particiona os dados em arquivos específicos de `temperaturas.csv` e `condicoes.csv`.



## 🛠️ Boas Práticas de Engenharia de Dados
* **Idempotência**: A DAG pode ser reexecutada para qualquer data passada sem gerar conflitos ou duplicação, graças ao uso de variáveis de execução do Airflow.
* **Segurança (Secret Management)**: Uso de variáveis de ambiente (`.env`) para que chaves de API nunca fiquem expostas no código-fonte.
* **Infraestrutura como Código**: Ambiente totalmente reproduzível através do Docker e Astro CLI.

## ⚙️ Como Executar o Projeto

### Pré-requisitos
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e rodando.
* [Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli) instalado.

### Passo a Passo
1.  **Clone este repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    cd SEU_REPOSITORIO
    ```

2.  **Configure a sua API Key:**
    Crie um arquivo chamado `.env` na raiz do projeto e adicione a sua chave:
    ```text
    AIRFLOW_VAR_VISUAL_CROSSING_KEY=COLOQUE_SUA_CHAVE_AQUI
    ```

3.  **Inicie os containers:**
    ```bash
    astro dev start
    ```

4.  **Acesse o Dashboard:**
    Vá para [http://localhost:8080](http://localhost:8080) e use as credenciais padrão (User: `admin` | Pass: `admin`).

---
**Desenvolvido por [Seu Nome]** [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](SEU_LINK_DO_LINKEDIN)
