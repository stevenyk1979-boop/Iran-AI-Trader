"""
Iran AI Trader Professional
Symbol Loader
"""

from market_data_adapter import MarketDataAdapter


class SymbolLoader:


    def __init__(self):

        self.adapter = MarketDataAdapter()



    def load_from_tsetmc(self, raw_data):

        """
        Convert TSETMC response
        into project symbols
        """

        return self.adapter.load_symbols(raw_data)



    def count(self, symbols):

        return len(symbols)