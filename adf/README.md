# 🔄 Azure Data Factory (ADF) Pipelines

This project uses Azure Data Factory (ADF) to orchestrate end-to-end data ingestion and transformation workflows for the Healthcare RCM platform.

---

## 📌 Overview

ADF acts as the **orchestration layer**, responsible for:

* Ingesting data from multiple sources
* Managing dependencies
* Triggering Databricks notebooks
* Enabling scalable, config-driven pipelines

---

## ⚙️ Pipeline Design

The pipelines follow a **config-driven architecture**, allowing dynamic execution for multiple datasets and hospitals without hardcoding logic.

---

## 🔑 Key Components

### 1. Linked Services

* Azure SQL Database (EMR data)
* ADLS Gen2 (storage)
* Azure Databricks
* Azure Key Vault (secrets)

📸
![Linked Services](screenshots/01_linked_services.png)

---

### 2. Parameterized Linked Services

* Enables dynamic connection handling
* Supports multiple hospital data sources

📸
![Parameterized LS](screenshots/02_linked_service_parameterized.png)

---

### 3. Datasets

* SQL datasets for EMR tables
* ADLS datasets for file storage
* Parameterized datasets for reusability

📸
![Datasets](screenshots/03_datasets_overview.png)

📸
![SQL Dataset](screenshots/04_dataset_sql_db.png)

---

## 🔄 Pipeline Flow

### 4. Source → Landing Pipeline

* Extracts data from source systems
* Loads into ADLS (Landing/Bronze)

📸
![Pipeline](screenshots/05_pipeline_src_landing.png)

---

### 5. ForEach Loop (Dynamic Execution)

* Iterates over config-driven table list
* Enables scalable ingestion

📸
![ForEach](screenshots/05a_foreach_loop.png)

---

### 6. Execute Pipeline Activity

* Calls child pipelines dynamically
* Separates logic for modular design

📸
![Execute Pipeline](screenshots/05b_execute_pipeline.png)

---

### 7. Copy Activity (Core Ingestion Logic)

* Handles both:

  * Full load
  * Incremental load (watermark-based)

📸
![Copy Flow](screenshots/05c_copy_activity_flow.png)

---

### 8. Silver & Gold Execution

* Triggers Databricks notebooks
* Processes Bronze → Silver → Gold transformations

📸
![Silver Gold](screenshots/06_silver_gold_pipeline.png)

---

### 9. Main Orchestration Pipeline

* Entry point for full workflow
* Coordinates ingestion + transformation

📸
![Main Pipeline](screenshots/07_main_pipeline_trigger.png)

---

## 💡 Key Highlights

* Config-driven ingestion using Lookup + ForEach
* Incremental loading using watermark strategy
* Modular pipeline design using Execute Pipeline
* Integration with Databricks for transformations
* Secure credential handling via Key Vault

---

## ✅ Summary

ADF serves as the backbone of the pipeline, enabling:

* Automation
* Scalability
* Reusability
* Maintainability
