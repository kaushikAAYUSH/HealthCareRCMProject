# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS ayush_rcm_project_databricks_ws.audit;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS ayush_rcm_project_databricks_ws.audit.load_logs (
# MAGIC     data_source STRING,
# MAGIC     tablename STRING,
# MAGIC     numberofrowscopied INT,
# MAGIC     watermarkcolumnname STRING,
# MAGIC     loaddate TIMESTAMP
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC truncate table ayush_rcm_project_databricks_ws.audit.load_logs

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from audit.load_logs

# COMMAND ----------

transaction_df = spark.read.parquet('abfss://bronze@ayushproject2sa.dfs.core.windows.net/hosb/transactions')
display(transaction_df)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COALESCE(CAST(MAX(loaddate) AS DATE), '1900-01-01') AS last_fetched_date FROM audit.load_logs WHERE data_source = 'hos-b' AND tablename = 'dbo.transactions'

# COMMAND ----------


