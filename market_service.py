"""
Iran AI Trader Professional
Market Service
"""

from market_config import DATA_SOURCE

from csv_provider import CSVProvider
from tsetmc_provider import TSETMCProvider


class MarketService:

    def __init__(self):

        if DATA_SOURCE.upper() == "TSETMC":

            self.provider = TSETMCProvider()

        else:

            self.provider = CSVProvider()

    def symbols(self):

        return self.provider.get_symbols()

    def history(self, symbol):

        return self.provider.get_history(symbol)

    def available(self):

        return self.provider.is_available()