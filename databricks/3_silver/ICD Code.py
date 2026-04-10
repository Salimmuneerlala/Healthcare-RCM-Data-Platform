# Databricks notebook source
#Read ICD extracts from bronze layer
df=spark.read.format("parquet").load("abfss://bronze@rcmstorageadls.dfs.core.windows.net/icd_codes/")

df.createOrReplaceTempView("staging_icd_codes")


# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS silver.icd_codes (
# MAGIC     icd_code STRING,
# MAGIC     icd_code_type STRING,
# MAGIC     code_description STRING,
# MAGIC     inserted_date DATE,
# MAGIC     updated_date DATE,
# MAGIC     is_current_flag BOOLEAN
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO
# MAGIC   silver.icd_codes AS target
# MAGIC USING
# MAGIC   staging_icd_codes AS source
# MAGIC ON target.icd_code = source.icd_code
# MAGIC WHEN MATCHED AND
# MAGIC   target.code_description != source.code_description
# MAGIC   THEN UPDATE SET
# MAGIC   target.code_description = source.code_description,
# MAGIC   target.updated_date = source.updated_date,
# MAGIC   target.is_current_flag = False
# MAGIC WHEN NOT MATCHED 
# MAGIC THEN INSERT (
# MAGIC     icd_code, 
# MAGIC     icd_code_type, 
# MAGIC     code_description, 
# MAGIC     inserted_date, 
# MAGIC     updated_date, 
# MAGIC     is_current_flag
# MAGIC   )
# MAGIC   VALUES (
# MAGIC     source.icd_code,
# MAGIC     source.icd_code_type,
# MAGIC     source.code_description,
# MAGIC     source.inserted_date,
# MAGIC     source.updated_date,
# MAGIC     source.is_current_flag
# MAGIC   )

# COMMAND ----------

