from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import plotly.express as px
import pandas as pd
import json

from vanna_setup import create_vanna_agent
from vanna.core.user import User

app = FastAPI()

# Initialize Vanna agent
agent, memory = create_vanna_agent()

# Default user required by Vanna
user = User(id="default_user")


class QuestionRequest(BaseModel):
    question: str


def clean_sql(sql: str) -> str:
    """Clean SQL from markdown or extra text."""
    if not sql:
        return ""

    sql = sql.strip()

    # Remove markdown ```sql ```
    if "```" in sql:
        sql = sql.replace("```sql", "").replace("```", "")

    # Remove text before SELECT
    select_index = sql.upper().find("SELECT")
    if select_index != -1:
        sql = sql[select_index:]

    # Remove semicolon
    sql = sql.replace(";", "")

    return sql.strip()


def validate_sql(sql: str) -> bool:
    """Allow only SELECT queries."""
    forbidden = ["INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "EXEC", "GRANT", "REVOKE", "SHUTDOWN"]
    sql_upper = sql.upper()

    if not sql_upper.startswith("SELECT"):
        return False

    for word in forbidden:
        if word in sql_upper:
            return False

    if "SQLITE_MASTER" in sql_upper:
        return False

    return True


@app.get("/")
def home():
    return {"message": "NL2SQL API is running"}


@app.get("/health")
def health():
    return {
        "status": "ok",
        "database": "connected"
    }


@app.post("/chat")
async def chat(request: QuestionRequest):
    question = request.question

    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    try:
        # UPDATED PROMPT WITH DATABASE SCHEMA (IMPORTANT FIX)
        prompt = f"""
You are a SQL generator for a SQLite database.

IMPORTANT:
Use only the tables and columns listed below.
Do not invent tables.
Do not invent columns.
Return ONLY SQL query.
Use only SELECT.

Database Schema:

patients(id, first_name, last_name, email, phone, date_of_birth, gender, city, registered_date)

doctors(id, name, specialization, department, phone)

appointments(id, patient_id, doctor_id, appointment_date, status, notes)

treatments(id, appointment_id, treatment_name, cost, duration_minutes)

invoices(id, patient_id, invoice_date, total_amount, paid_amount, status)

Question: {question}
"""

        # Vanna async generator response
        response_text = ""
        async for chunk in agent.send_message(user, prompt):
            if hasattr(chunk, "simple_component") and chunk.simple_component:
                response_text += chunk.simple_component.text

        print("\n=== RAW RESPONSE ===")
        print(response_text)
        print("=====================\n")

        # Extract SQL from response text
        sql_query = clean_sql(response_text)

        print("=== CLEANED SQL ===")
        print(sql_query)
        print("===================\n")

        # Validate SQL
        if not validate_sql(sql_query):
            raise HTTPException(status_code=400, detail="Invalid SQL generated")

        # Execute SQL
        conn = sqlite3.connect("clinic.db")
        df = pd.read_sql_query(sql_query, conn)
        conn.close()

        # If no data
        if df.empty:
            return {
                "message": "No data found",
                "sql_query": sql_query,
                "columns": [],
                "rows": [],
                "row_count": 0,
                "chart": {},
                "chart_type": ""
            }

        # Generate chart if possible
        chart = {}
        chart_type = ""
        if len(df.columns) >= 2:
            fig = px.bar(df, x=df.columns[0], y=df.columns[1])
            chart = json.loads(fig.to_json())
            chart_type = "bar"

        return {
            "message": "Query executed successfully",
            "sql_query": sql_query,
            "columns": list(df.columns),
            "rows": df.values.tolist(),
            "row_count": len(df),
            "chart": chart,
            "chart_type": chart_type
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))