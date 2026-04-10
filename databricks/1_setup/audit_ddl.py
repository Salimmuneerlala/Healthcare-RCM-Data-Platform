# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS rcm_project_dbws.audit;
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS rcm_project_dbws.audit.load_logs (
# MAGIC     data_source STRING,
# MAGIC     tablename STRING,
# MAGIC     numberofrowscopied INT,
# MAGIC     watermarkcolumnname STRING,
# MAGIC     loaddate TIMESTAMP
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from rcm_project_dbws.audit.load_logs;

# COMMAND ----------

# MAGIC %sql
# MAGIC truncate table rcm_project_dbws.audit.load_logs;

# COMMAND ----------

