"""
Iran AI Trader Professional
CSV Provider
"""

import os

from market_provider import MarketProvider
from csv_loader import CSVLoader
from symbol_alias import SymbolAlias


class CSVProvider(MarketProvider):

    def __init__(self):

        self.csv_loader = CSVLoader()

        self.alias = SymbolAlias()

    def get_symbols(self):

        symbols = []

        used = set()

        folder = "market_data"

        if not os.path.exists(folder):

            return symbols

        for filename in os.listdir(folder):

            if not filename.endswith(".csv"):

                continue

            symbol = filename.replace(".csv", "")

            symbol = self.alias.normalize(symbol)

            if symbol in used:

                continue

            used.add(symbol)

            symbols.append({

                "symbol": symbol,

                "file": os.path.join(

                    folder,

                    filename

                )

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