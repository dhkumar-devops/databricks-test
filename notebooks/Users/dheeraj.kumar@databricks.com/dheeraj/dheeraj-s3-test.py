# Databricks notebook source
dbutils.fs.ls("s3a://dheeraj-data-bucket")

# COMMAND ----------

dbutils.fs.cat("s3a://dheeraj-data-bucket/export.csv")