# Airflow-domain-etl
# From Scripts to Systems: A Personal Data Engineering Project with Apache Airflow

This repository contains a **personal data engineering project** built while learning how to design, orchestrate, and automate data pipelines using **Apache Airflow**.

The goal of this project is not just to move data from point A to point B, but to understand how real-world data engineering systems are structured, monitored, and maintained.

This project is also documented in a Medium article where I share my learning experience, challenges, and key takeaways.

---

## 📌 Project Overview

The project implements a **basic but realistic ETL (Extract, Transform, Load) pipeline** using Apache Airflow.

### What the pipeline does:
1. **Extract** a publicly available dataset (CSV) from Kaggle
2. **Transform** the data using Python (cleaning, filtering, basic aggregation)
3. **Load** the processed data into a local storage layer
4. **Orchestrate** the workflow using Airflow DAGs with task dependencies

The pipeline is designed to be:
- Reproducible
- Observable
- Easy to extend
- Suitable for local or cloud-based development

---

## 🧠 Why This Project?

Before this project, most of my work involved running scripts manually. As the project evolved, I realized that real data engineering requires:
- Explicit task dependencies
- Retry mechanisms
- Execution history and logs
- Automation instead of manual runs

Apache Airflow helped bridge that gap by turning scripts into **reliable systems**.

---

## 🛠️ Tech Stack

- **Apache Airflow** – Workflow orchestration
- **Python** – Data extraction and transformation
- **Docker & Docker Compose** – Environment setup
- **GitHub Codespaces** – Cloud-based development
- **Kaggle Dataset** – Public data source

---

## 📂 Project Structure
.
├── dags/
│ └── basic_etl_pipeline.py # Airflow DAG definition
├── data/
│ ├── raw/ # Raw extracted data
│ └── processed/ # Transformed output data
├── docker-compose.yaml # Airflow services
├── requirements.txt # Python dependencies
├── README.md # Project documentation


---

## 🔄 The ETL Pipeline

The Airflow DAG consists of three core tasks:
extract_data → transform_data → load_data


- **Extract**: Downloads and validates raw data
- **Transform**: Cleans and processes the dataset
- **Load**: Saves the processed output for downstream use

Each task is isolated, idempotent, and easy to debug.

---

## 🚀 Running the Project

### Option 1: GitHub Codespaces (Recommended)

GitHub Codespaces allows you to run the entire project in the cloud without installing anything locally.

**Steps:**
1. Fork this repository
2. Click **Code → Open with Codespaces**
3. Wait for the environment to initialize
4. Start Airflow using Docker Compose
5. Access the Airflow UI via the forwarded port

Once running, Airflow will automatically detect DAGs in the `dags/` directory.

---

### Option 2: Run Locally

**Requirements:**
- Python 3.9+
- Docker
- Docker Compose

**Steps:**
1. Clone the repository
2. Set up the environment variables
3. Start Airflow services
4. Open the Airflow UI at `http://localhost:8080`
5. Trigger the DAG manually or via schedule

---

## 📊 Dataset

The project uses a **free, publicly available dataset from Kaggle**.

- Dataset format: CSV
- Domain: Open data suitable for batch processing
- Purpose: Demonstrate realistic extract and transform operations

*(Dataset details and screenshots are referenced in the Medium article.)*

---

## 🧪 What This Project Demonstrates

- Understanding of ETL principles
- Practical use of Apache Airflow DAGs and tasks
- Workflow orchestration and dependency management
- Logging, retries, and observability
- Cloud-based development using GitHub Codespaces
- Writing maintainable, readable pipeline code

---

## ✍️ Related Article

This project is accompanied by a Medium article where I explain:
- What I learned while building this pipeline
- How my mindset shifted from scripts to systems
- Why orchestration matters in data engineering

📖 *Link to article coming soon*

---

## 🔮 Possible Improvements

- Add data validation checks
- Store output in a database instead of local files
- Parameterize DAGs for multiple datasets
- Add alerting and monitoring
- Deploy to a managed Airflow service

---

## 📬 Final Notes

This project was built as a **learning exercise**, but it mirrors many of the patterns used in real production data pipelines.

If you’re learning data engineering, building a small project like this is one of the fastest ways to understand how everything fits together.

---

**Author:** Vidit Parekh  
**Focus:** Data Engineering | Apache Airflow | ETL Pipelines  

