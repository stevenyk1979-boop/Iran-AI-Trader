"""
Iran AI Trader V2.0
Database Manager
"""

import sqlite3
from pathlib import Path

from config import DATABASE_PATH


class DatabaseManager:
    def __init__(self):
        self.db_path = Path(DATABASE_PATH)

    def connect(self):
        return sqlite3.connect(self.db_path)

    def initialize(self):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS portfolio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            quantity REAL,
            buy_price REAL,
            create_date TEXT
        )
        """)

        conn.commit()
        conn.close()

        print("Database initialized successfully.")