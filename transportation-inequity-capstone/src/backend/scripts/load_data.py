#!/usr/bin/env python3
"""Load cleaned CSV into the project's SQLite database.

Usage: python3 load_data.py [path/to/cleaned.csv]
"""
import sys
import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_CSV = os.path.join(BASE_DIR, "src/data/processed/clean_transportation.csv")
DB_PATH = os.path.join(BASE_DIR, "transportation.db")


def load(csv_path: str = None):
    path = csv_path or DEFAULT_CSV
    if not os.path.exists(path):
        print(f"CSV not found: {path}")
        return

    df = pd.read_csv(path)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("commute_data", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Loaded {len(df)} rows into {DB_PATH}")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    load(arg)
