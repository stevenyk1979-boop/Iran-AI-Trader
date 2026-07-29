"""
Iran AI Trader Professional
Market Universe
"""


class MarketUniverse:

    def __init__(self):

        self.symbols = []

    def load(self, symbols):

        self.symbols = list(symbols)

    def all(self):

        return self.symbols

    def count(self):

        return len(self.symbols)

    def clear(self):

        self.symbols.clear()

    def exists(self, symbol):

        return symbol in self.symbols