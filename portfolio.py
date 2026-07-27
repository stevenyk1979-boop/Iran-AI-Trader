"""
Iran AI Trader V2.0
Portfolio Manager
"""

import sqlite3

from config import DATABASE_PATH


class PortfolioManager:

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)

    def list_assets(self):

        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT symbol,
                   quantity,
                   buy_price
            FROM portfolio
        """)

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("Portfolio is empty.")
            return

        print("\nCurrent Portfolio")
        print("-" * 40)

        for row in rows:
            print(
                f"{row[0]} | Qty: {row[1]} | Buy: {row[2]}"
            )

    def add_asset(
        self,
        symbol,
        quantity,
        buy_price
    ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO portfolio
            (
                symbol,
                quantity,
                buy_price
            )
            VALUES
            (
                ?,
                ?,
                ?
            )
            """,
            (
                symbol,
                quantity,
                buy_price
            ),
        )

        self.connection.commit()

        print(f"{symbol} added.")