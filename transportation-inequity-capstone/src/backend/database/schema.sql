-- Schema for commute data
CREATE TABLE IF NOT EXISTS commute_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    region TEXT,
    avg_commute_time REAL,
    total_workers INTEGER,
    no_vehicle_workers INTEGER
);
