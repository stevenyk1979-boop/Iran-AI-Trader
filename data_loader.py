"""
Iran AI Trader V2.0
Data Loader
"""

from datetime import datetime


class DataLoader:

    def __init__(self):
        self.market = "Iran Stock Market"

    def connect(self):
        print(f"Connecting to {self.market}...")

    def load_symbols(self):

        symbols = [
            "فملی",
            "فولاد",
            "شستا",
            "خودرو",
            "وبملت",
        ]

        return symbols

    def update(self):

        self.connect()

        symbols = self.load_symbols()

        print(f"Loaded {len(symbols)} symbols")

        for symbol in symbols:
            print(" -", symbol)

        print("Update Time:", datetime.now())