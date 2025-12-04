# Main entry point for the transportation inequity capstone project
from fastapi import FastAPI
import sqlite3
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, "transportation.db")

def get_data():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM commute_data LIMIT 20")
        rows = cursor.fetchall()
    except Exception as e:
        rows = []
        print(f"Error querying database: {e}")
    conn.close()
    return [dict(row) for row in rows]

@app.get("/")
def root():
    return {"message": "Transportation Inequity Capstone API", "endpoints": ["/commute_stats"]}

@app.get("/commute_stats")
def commute_stats():
    return get_data()
