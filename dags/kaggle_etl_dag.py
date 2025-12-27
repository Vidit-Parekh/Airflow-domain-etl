from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import os

DATA_DIR = os.path.join(os.getcwd(), "data")
RAW_FILE = os.path.join(DATA_DIR, "raw_websites.csv")
OUTPUT_FILE = os.path.join(DATA_DIR, "tld_summary.csv")


def extract():
    if not os.path.exists(RAW_FILE):
        raise FileNotFoundError("Kaggle dataset not found")
    print("Dataset extracted successfully")


def transform():
    df = pd.read_csv(RAW_FILE, names=["rank", "domain"])
    df["tld"] = df["domain"].apply(lambda x: x.split('.')[-1])
    summary = df["tld"].value_counts().reset_index()
    summary.columns = ["tld", "count"]
    summary.to_csv(OUTPUT_FILE, index=False)
    print("Transformation completed")


def load():
    df = pd.read_csv(OUTPUT_FILE)
    print(df.head(10))


with DAG(
    dag_id="kaggle_domain_etl",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["etl", "airflow", "kaggle"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id="load_data",
        python_callable=load
    )

    extract_task >> transform_task >> load_task
