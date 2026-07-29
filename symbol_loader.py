"""
Iran AI Trader Professional
Symbol Loader
"""

from market_data_adapter import MarketDataAdapter
from market_universe import MarketUniverse


class SymbolLoader:


    def __init__(self):

        self.adapter = MarketDataAdapter()

        self.universe = MarketUniverse()



    def load_from_tsetmc(self, raw_data):

        """
        Convert TSETMC raw data
        into project symbol format
        """

        return self.adapter.load_symbols(raw_data)



    def load_universe(self, raw_data):

        """
        Load symbols into Market Universe
        """

        symbols = self.load_from_tsetmc(raw_data)

        self.universe.load(symbols)

        return self.universe



    def get_universe(self):

        """
        Return current market universe
        """

        return self.universe



    def get_symbols(self):

        """
        Return current symbols
        """

        return self.universe.symbols()



    def count(self):

        """
        Return symbol count
        """

        return self.universe.count()