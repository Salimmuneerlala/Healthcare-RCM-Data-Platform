# Healthcare RCM Data Platform Architecture

## Overview

This project follows a **Medallion Architecture (Landing → Bronze → Silver → Gold)** to process healthcare Revenue Cycle Management (RCM) data from multiple sources and transform it into analytics-ready datasets.

---

## 🔄 Data Sources

The system integrates data from multiple heterogeneous sources:

1. **EMR Data (Azure SQL Database)**
   - Patient, Provider, Department, Encounter, Transaction tables
   - Multiple hospitals with different schemas

2. **Flat Files (ADLS Gen2 - CSV)**
   - Claims data (insurance)
   - CPT codes (procedure data)

3. **External APIs**
   - NPI API → Provider details
   - ICD API → Disease classification

---

## ⚙️ Ingestion Layer (Landing → Bronze)

### Azure Data Factory (ADF)

ADF is used for orchestrating ingestion pipelines using a **config-driven approach**.

### Key Features:
- Lookup activity reads config file
- ForEach iterates through tables
- Supports:
  - Full load
  - Incremental load (watermark-based)
- Archives existing files before ingestion

### Incremental Logic:
- Fetch last load date from audit table
- Default fallback: `1900-01-01`
- Load only new/updated records

---

## 🥉 Bronze Layer (Raw Standardized Data)

- Stores raw data in **Parquet format**
- No transformations applied
- Data is stored as-is from sources

### Sources:
- SQL → via ADF
- CSV → via Databricks
- API → via Databricks

---

## 🥈 Silver Layer (Cleaned & Modeled Data)

This layer performs:

### Data Cleaning
- Null handling
- Filtering invalid records

### Data Quality
- `is_quarantine` flag for bad records

### Common Data Model (CDM)
- Standardizes schema across hospitals
- Creates surrogate keys:
-  `patient_key` = patient_id + datasource

### SCD Type 2 Implementation
- Tracks historical changes
- Maintains:
- is_current flag
- effective_date
- expiry_date

---

## 🥇 Gold Layer (Business Ready Data)

This layer contains **dimensional models (Star Schema)**:

### Dimension Tables:
- Patient
- Provider
- Department
- ICD
- NPI
- CPT Codes

### Fact Tables:
- Transactions
- Claims

### Features:
- Filtered clean data
- Aggregated metrics
- Optimized for analytics

---

## 🔄 Orchestration

- ADF triggers:
- Ingestion pipelines
- Databricks notebooks
- Ensures end-to-end automation

---

## Output

- Analytics-ready datasets
- Can be consumed by:
- Power BI
- Reporting tools
- ML models
