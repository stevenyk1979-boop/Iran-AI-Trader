"""
Iran AI Trader Professional
CSV Provider
"""

import os

from market_provider import MarketProvider
from csv_loader import CSVLoader


class CSVProvider(MarketProvider):

    def __init__(self):
        self.csv_loader = CSVLoader()

    def get_symbols(self):

        symbols = []

        folder = "market_data"

        if not os.path.exists(folder):
            return symbols

        for filename in os.listdir(folder):

            if filename.endswith(".csv"):

                symbols.append({
                    "symbol": filename.replace(".csv", ""),
                    "file": os.path.join(folder, filename)
                })

        return symbols

    def get_history(self, symbol):

        filename = os.path.join(
            "market_data",
            f"{symbol}.csv"
        )

        return self.csv_loader.load(filename)

    def is_available(self):
        return True