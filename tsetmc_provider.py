"""
Iran AI Trader Professional
TSETMC Provider
"""

from market_provider import MarketProvider

from tsetmc_connector import TSETMCConnector
from tsetmc_history import TSETMCHistory


class TSETMCProvider(MarketProvider):

    def __init__(self):

        self.connector = TSETMCConnector()

        self.connector.connect()

        self.history = TSETMCHistory(self.connector)

    def get_symbols(self):

        return self.connector.get_symbols()

    def get_history(self, symbol):

        return self.history.get_history(symbol)

    def is_available(self):

        return self.connector.status()