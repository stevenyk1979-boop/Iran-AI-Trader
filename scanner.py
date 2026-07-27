"""
Iran AI Trader V2.0
Market Scanner
"""

from data_loader import DataLoader


class Scanner:

    def __init__(self):

        self.loader = DataLoader()

    def scan(self):

        symbols = self.loader.load_symbols()

        print()
        print("=" * 40)
        print("Market Scanner")
        print("=" * 40)

        for index, symbol in enumerate(symbols, start=1):

            print(f"{index}. {symbol}")

        print()
        print(f"{len(symbols)} symbols scanned.")