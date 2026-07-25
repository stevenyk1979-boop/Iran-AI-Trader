import sqlite3
from config import DATABASE_PATH


class DatabaseManager:

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)

    def initialize(self):

        cursor = self.connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS portfolio(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT,
            quantity REAL,
            buy_price REAL
        )
        """)

        self.connection.commit()

        print("Database Ready")