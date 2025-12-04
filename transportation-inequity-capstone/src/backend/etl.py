import pandas as pd
import os
import sqlite3

# Get absolute paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_PATH = os.path.join(BASE_DIR, "src/data/raw/transportation.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "src/data/processed/clean_transportation.csv")
DB_PATH = os.path.join(BASE_DIR, "transportation.db")

def clean_commute_data():
    df = pd.read_csv(RAW_PATH)

    # Example cleanup
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Drop empty rows
    df.dropna(how="all", inplace=True)

    # Keep key columns (adjust once you view your real file)
    keep_cols = [
        "geography",
        "mean_travel_time_to_work",
        "total_workers",
        "workers_no_vehicle"
    ]
    df = df[[col for col in keep_cols if col in df.columns]]

    df.to_csv(OUTPUT_PATH, index=False)

    print("✅ Cleaned commute data saved to:", OUTPUT_PATH)
    return df

def load_to_sqlite(df):
    conn = sqlite3.connect(DB_PATH)
    
    # Only rename if we have the expected columns
    if len(df.columns) > 1:
        df_to_save = df.copy()
        df_to_save.to_sql("commute_data", conn, if_exists="replace", index=False)
        print("✅ Data loaded into SQLite database")
    else:
        print("⚠️ Data has unexpected structure, skipping SQLite load")
    
    conn.close()

if __name__ == "__main__":
    df = clean_commute_data()
    load_to_sqlite(df)
