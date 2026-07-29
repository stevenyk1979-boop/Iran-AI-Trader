"""
Iran AI Trader V2.0 Beta
Market Cache
"""


class MarketCache:

    def __init__(self):

        self.cache = {}

    def save(self, symbol, prices):

        self.cache[symbol] = prices

    def load(self, symbol):

        return self.cache.get(symbol)

    def clear(self):

        self.cache.clear()

    def size(self):

        return len(self.cache)

    def symbols(self):

        return list(self.cache.keys())