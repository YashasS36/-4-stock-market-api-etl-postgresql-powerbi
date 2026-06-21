# 🚀 Real-Time Stock Market Data Pipeline using WayFinance API, Python, PostgreSQL & Power BI

## 📌 Project Overview

This project demonstrates an end-to-end **Real-Time Stock Market Data Pipeline** built using Data Engineering concepts.

The objective of this project was to extract stock market data from the **WayFinance API**, perform ETL operations using Python, store the processed data in PostgreSQL, perform SQL-based analytics, and create an interactive Power BI dashboard for data visualization.

This project represents my **4th project out of my 7-project Data Engineering roadmap**, focusing on API integration, ETL pipeline development, database management, SQL analytics, and business intelligence reporting.


# 🏗️ Project Architecture


yFinance API
|
↓
Python Data Extraction
|
↓
Data Transformation
|
↓
PostgreSQL Database
|
↓
SQL Analytics
|
↓
Power BI Dashboard

The complete workflow follows:

**Extract → Transform → Load → Analyze → Visualize**

# 🎯 Project Objectives

The main objectives of this project are:

- Extract stock market data from an external API source
- Build an ETL pipeline using Python
- Transform raw API data into a structured format
- Load processed data into PostgreSQL
- Perform SQL analytics on stock market data
- Create an interactive Power BI dashboard
- Understand a complete real-world data engineering workflow

# 🔄 Data Pipeline Workflow

## 1️⃣ Data Extraction using WayFinance API

The first stage of the pipeline involved extracting stock market data from the **WayFinance API**.

### Process:

- Connected Python scripts with the API endpoint
- Extracted the last one month of stock market data
- Retrieved raw financial data in JSON format
- Converted API responses into structured datasets

### Technologies Used:

- Python
- REST API
- JSON Data Processing

# 2️⃣ Data Transformation using Python

After extraction, the raw API data was transformed into an analysis-ready dataset.

### Transformation Activities:

- Cleaned raw stock market data
- Structured required columns
- Formatted data types
- Prepared the dataset for database loading

The transformed data was converted into a clean format suitable for analytics.

# 3️⃣ Data Loading into PostgreSQL

The transformed stock market data was loaded into PostgreSQL.

### Database Implementation:

- Created PostgreSQL database
- Designed stock market data table
- Loaded processed records
- Stored structured financial information

### Main Table:

stock_data

PostgreSQL was used as the centralized database layer for storing and analyzing stock market data.

# 4️⃣ SQL Analytics

After loading the data into PostgreSQL, SQL queries were created to analyze the stock market dataset.

### Analytics Performed:

- Stock price analysis
- Market trend analysis
- Trading volume analysis
- Stock performance comparison
- Financial data exploration

SQL helped convert stored data into meaningful analytical insights.

# 5️⃣ Power BI Dashboard Development

The PostgreSQL database was connected with **Power BI Desktop** to create an interactive dashboard.

The dashboard provides clear visualization of stock market trends and performance metrics.

### Dashboard Features:

- Stock market overview
- Price movement analysis
- Volume analysis
- Performance indicators
- Interactive filters and visuals

The dashboard helps users understand stock market behavior through data-driven insights.

# 🛠️ Technology Stack

## Programming Language

- Python

## Data Source

- yFinance API

## Database

- PostgreSQL

## Query Language

- SQL

## Visualization

- Microsoft Power BI Desktop

## Development Tools

- Visual Studio Code
- GitHub

# 📂 Project Structure


real-time-stock-market-data-pipeline

│
├── Architecture
│ └── Architecture Diagram
│
├── Data
│
├── Scripts
│ ├── extract.py
│ ├── transform.py
│ └── load.py
│
├── Output
│
├── SQL
│ └── analytics_queries.sql
│
├── PowerBI Dashboard
│
├── README.md
│
└── requirements.txt

# 📊 Project Screenshots

## Architecture Diagram

The architecture represents the complete flow of data from API extraction to dashboard visualization.

## API Data Extraction

Stock market data was extracted from WayFinance API using Python scripts.

## Python ETL Scripts

Python scripts were used for extracting, transforming, and preparing data for database loading.

## PostgreSQL Database

Processed stock market data was stored in PostgreSQL for structured storage and analysis.

## PostgreSQL Table Data

The cleaned stock market dataset was loaded into the `stock_data` table.

## SQL Analytics

SQL queries were performed to generate insights from the stock market data.

## Power BI Dashboard

Power BI was used to create interactive visualizations and present analytical insights.

# 📈 Skills Demonstrated

Through this project, I gained practical experience in:

✅ API Integration  
✅ ETL Pipeline Development  
✅ Python Data Processing  
✅ Data Transformation  
✅ PostgreSQL Database Management  
✅ SQL Analytics  
✅ Power BI Dashboard Development  
✅ End-to-End Data Engineering Workflow  

# 💡 Key Learnings

This project helped me understand how real-world data engineering systems are designed.

Starting from extracting raw financial data through APIs, transforming and storing it in a database, performing analytical queries, and finally creating dashboards, this project provided hands-on experience with the complete data lifecycle.


# 🚀 Future Enhancements

Future improvements for this project include:

- Automating scheduled API data ingestion
- Implementing cloud storage solutions
- Adding real-time streaming capabilities
- Deploying the pipeline on cloud platforms
- Implementing monitoring and logging


# 📌 Data Engineering Roadmap Progress

This project is **Project #4 out of my 7-project Data Engineering roadmap**.

Completed Projects:

✅ Project 1: Sales Data ETL Pipeline  
✅ Project 2: E-Commerce Data Warehouse Project  
✅ Project 3: Azure + Databricks Sales Analytics Pipeline  
✅ Project 4: Real-Time Stock Market Data Pipeline  

Upcoming Projects:

🔹 Retail Analytics Data Warehouse  
🔹 Weather Data Engineering Pipeline  
🔹 End-to-End Data Lake Project  


# 👨‍💻 Author

**Yashas S**

Aspiring Data Engineer

Skills:
Python | SQL | PostgreSQL | Power BI | Azure | Databricks | ETL

---

⭐ If you find this project useful, consider giving t
