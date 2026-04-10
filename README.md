# 🏥 Healthcare Revenue Cycle Management (RCM) Data Platform

## Overview
Built an end-to-end Azure Data Engineering solution to process healthcare financial data from multiple sources.

## Tech Stack
- Azure Data Factory (ETL orchestration)
- Azure Databricks (data processing)
- ADLS Gen2 (storage)
- Delta Lake (data reliability)

## Medallion Architecture
Landing → Bronze → Silver → Gold

## Data Sources
- EMR Data (Azure SQL DB)
- Claims CSV Files (ADLS)
- APIs (NPI, ICD)

## Key Features
- Config-driven ingestion pipelines
- Incremental & full load support
- SCD Type 2 implementation
- Data quality checks with quarantine logic

## Project Structure
- `adf/` → pipeline screenshots & configs
- `databricks/` → notebooks (bronze, silver, gold)
- `configs/` → ingestion config
- `docs/` → architecture details

## ADF Pipeline
See `/adf/screenshots`

## Architecture Diagram
![Architecture](docs/images/architecture.png)

## Data Model (Star Schema)
![Data Model](docs/images/data_model.png)

---

⭐ This project demonstrates real-world data engineering practices using Azure.
