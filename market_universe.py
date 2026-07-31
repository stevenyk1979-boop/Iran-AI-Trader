"""
Iran AI Trader Professional
Market Universe
"""

from symbol_manager import SymbolManager
from symbol_alias import SymbolAlias


class MarketUniverse:

    def __init__(self):

        self.symbol_manager = SymbolManager()

        self.alias = SymbolAlias()

        self.market = "Iran Stock Market"

    def load(self, symbols):

        """
        Load market symbols
        Remove duplicates
        Normalize aliases
        """

        clean = []

        used = set()

        for item in symbols:

            symbol = self.alias.normalize(

                item["symbol"]

            )

            if symbol in used:

                continue

            used.add(symbol)

            new_item = dict(item)

            new_item["symbol"] = symbol

            clean.append(new_item)

        self.symbol_manager.load(clean)

    def symbols(self):

        return self.symbol_manager.all()

    def count(self):

        return self.symbol_manager.count()

    def exists(self, symbol):

        symbol = self.alias.normalize(symbol)

        return self.symbol_manager.exists(symbol)

    def search(self, keyword):

        return self.symbol_manager.find(keyword)

    def clear(self):

        self.symbol_manager.symbols = []

    def status(self):

        return {

            "market": self.market,

            "symbols": self.count()

        }