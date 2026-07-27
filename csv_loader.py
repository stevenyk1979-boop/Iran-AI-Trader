"""
Iran AI Trader V2.0
CSV Loader
"""

import csv
from datetime import datetime

from historical_data import HistoricalData
from market_data import MarketData


class CSVLoader:

    def load(self, filename):

        history = HistoricalData()

        with open(filename, newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                candle = MarketData(

                    symbol=row["symbol"],

                    date=datetime.now(),

                    open_price=float(row["open"]),

                    high_price=float(row["high"]),

                    low_price=float(row["low"]),

                    close_price=float(row["close"]),

                    volume=int(row["volume"]),

                    value=float(row["value"])

                )

                history.add(candle)

        return history