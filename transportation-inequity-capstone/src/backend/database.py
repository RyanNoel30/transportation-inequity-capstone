import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_NAME = os.path.join(BASE_DIR, "transportation.db")

def create_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS commute_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        region TEXT,
        avg_commute_time REAL,
        total_workers INTEGER,
        no_vehicle_workers INTEGER
    );
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
# Database connection and management
