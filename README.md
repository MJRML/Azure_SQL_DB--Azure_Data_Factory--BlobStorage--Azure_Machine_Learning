# Jupyter Notebook -> Azure SQL DB -> Azure Data Factory -> Azure Blob Storage -> PreProcessing with Databricks -> Blob Storage

##  Project Overview

This project demonstrates a complete data pipeline workflow using Azure services, starting from local data ingestion to cloud-based preprocessing and storage. The solution integrates Jupyter Notebooks, Azure SQL Database, Azure Data Factory, Azure Blob Storage, and Azure Databricks for efficient data handling and transformation.

## Objectives

- Upload a dataset from a local development environment (Jupyter Notebook) to an Azure SQL Database using Python.

- Automate the transfer of data from Azure SQL Database to Azure Blob Storage using Azure Data Factory (ADF).

- Preprocess the dataset using Azure Databricks with PySpark.

- Store the cleaned and transformed data back in Azure Blob Storage for downstream use.

## Workflow Summary

- **Step 1: Upload Dataset to Azure SQL Database:**  
  The dataset is loaded and uploaded to an Azure SQL Database from a Jupyter Notebook using the sqlalchemy Python package.

- **Step 2: Transfer Data to Azure Blob Storage via Azure Data Factory:**  
  A pipeline in Azure Data Factory extracts the data from Azure SQL Database and writes it to a specified container in Azure Blob Storage in CSV format.

- **Step 3: Preprocess Data with Azure Databricks**  
  The data is read from Blob Storage into Azure Databricks using PySpark. Data cleaning, transformation, and preprocessing steps are applied. The refined dataset is then written back to Blob Storage in an       
  organized format for further use or analysis.

## Technologies Used
- Python (in Jupyter Notebook)

- Azure SQL Database

- Azure Data Factory (ADF)

- Azure Blob Storage

- Azure Databricks


