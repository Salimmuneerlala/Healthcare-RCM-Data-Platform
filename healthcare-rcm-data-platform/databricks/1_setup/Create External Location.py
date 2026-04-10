# Databricks notebook source
containers = ['landing', 'bronze', 'silver', 'gold']
for container in containers:
    spark.sql(f"""
    CREATE EXTERNAL LOCATION IF NOT EXISTS `rcm-project-ext-loc-{container}`
    URL 'abfss://{container}@rcmstorageadls.dfs.core.windows.net/'
    WITH (STORAGE CREDENTIAL `rcm-project-credentials`);
    """)

# COMMAND ----------

