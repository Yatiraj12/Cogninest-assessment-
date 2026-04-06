# AI-Powered Natural Language to SQL (NL2SQL) System

## Project Overview

This project is an AI-powered Natural Language to SQL (NL2SQL) system that allows users to ask questions in plain English and automatically converts them into SQL queries, executes them on a SQLite database, and returns structured results along with chart visualizations.

The system is built using **Vanna AI 2.0**, **Groq LLM (llama-3.3-70b-versatile)**, **FastAPI**, **SQLite**, **Pandas**, and **Plotly**.

This project demonstrates how Large Language Models (LLMs) can be integrated with databases to enable natural language data querying.

---

## Features

- Convert Natural Language → SQL
- SQL Query Validation (Only SELECT allowed)
- SQLite Database Execution
- Structured JSON Response
- Plotly Chart Generation
- Vanna Agent Memory Training
- FastAPI REST API
- Groq LLM Integration (llama-3.3-70b-versatile)
- End-to-End NL2SQL Pipeline

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| LLM | Groq (llama-3.3-70b-versatile) |
| NL2SQL Agent | Vanna AI 2.0 |
| Backend API | FastAPI |
| Database | SQLite |
| Data Processing | Pandas |
| Visualization | Plotly |
| Environment | Python 3.11 |
| API Testing | Swagger UI |

---

## System Architecture


User Question
↓
FastAPI API (/chat)
↓
Vanna AI Agent
↓
Groq LLM (llama-3.3-70b-versatile)
↓
Generated SQL Query
↓
SQL Validation (Only SELECT allowed)
↓
SQLite Database Execution
↓
Pandas DataFrame
↓
Plotly Chart Generation
↓
JSON Response (SQL + Data + Chart)


---

## Project Structure


project/
│
├── setup_database.py # Creates SQLite database and tables
├── seed_memory.py # Trains Vanna memory with sample questions
├── vanna_setup.py # Vanna Agent + Groq + SQLite setup
├── main.py # FastAPI application
├── requirements.txt # Dependencies
├── README.md # Project documentation
├── RESULTS.md # Test results
├── .env # API keys
└── clinic.db # SQLite database


---

## Database Schema

The system uses a clinic management database with the following tables:

### patients
- id
- first_name
- last_name
- email
- phone
- date_of_birth
- gender
- city
- registered_date

### doctors
- id
- name
- specialization
- department
- phone

### appointments
- id
- patient_id
- doctor_id
- appointment_date
- status
- notes

### treatments
- id
- appointment_id
- treatment_name
- cost
- duration_minutes

### invoices
- id
- patient_id
- invoice_date
- total_amount
- paid_amount
- status

---

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate
2. Install Dependencies
pip install -r requirements.txt
3. Add Groq API Key in .env
GROQ_API_KEY=your_groq_api_key_here
4. Setup Database
python setup_database.py
5. Train Vanna Memory
python seed_memory.py
6. Run FastAPI Server
uvicorn main:app --port 8000
7. Open Swagger UI
http://127.0.0.1:8000/docs
API Endpoint
POST /chat
Request
{
  "question": "How many patients do we have?"
}
Response
{
  "message": "Query executed successfully",
  "sql_query": "SELECT COUNT(*) FROM patients",
  "columns": ["COUNT(*)"],
  "rows": [[400]],
  "row_count": 1,
  "chart": {},
  "chart_type": ""
}
SQL Validation

For security, the system only allows SELECT queries.
The following SQL commands are blocked:

INSERT
UPDATE
DELETE
DROP
ALTER
EXEC
GRANT
REVOKE

This prevents database modification and SQL injection risks.

Memory Training (Vanna AI)

The system uses Vanna Agent Memory to improve SQL generation accuracy over time.
Sample training questions are stored so the agent learns common query patterns.

Example training questions:

How many patients do we have?
Show revenue by doctor
Top 5 patients by spending
Show unpaid invoices
Monthly appointment count
Chart Generation

If the SQL query returns 2 or more columns, the system automatically generates a Plotly bar chart and returns chart JSON in the response.

Example charts:

Revenue by month
Appointments per doctor
Patients by city
Top 5 patients by spending
LLM Used

Groq API with model:

llama-3.3-70b-versatile

Groq was used because it provides very fast inference for large language models, making NL2SQL queries fast and efficient.

Example Questions You Can Ask
How many patients do we have?
List doctor names and their specialization
Show unpaid invoices
Top 5 patients by total invoice amount
Which city has the most patients?
Average treatment cost
Number of appointments per doctor
Monthly revenue from invoices
How many appointments are completed?
Show total revenue from invoices
Results

See RESULTS.md for test queries, generated SQL, and accuracy results.

Conclusion

This project demonstrates how AI can be used to convert natural language into SQL queries and interact with databases without requiring SQL knowledge. The system is safe, scalable, and can be extended to support other databases like PostgreSQL or MySQL.

This project showcases:

LLM Integration
NL2SQL Systems
FastAPI Backend Development
SQL Validation & Security
Data Visualization
AI Agent Memory Systems
Author

AI Engineer Project – NL2SQL System using Vanna AI and Groq


---

