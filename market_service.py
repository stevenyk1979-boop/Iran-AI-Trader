"""
Iran AI Trader V2.0 Alpha
Market Service
"""

from market_repository import MarketRepository


class MarketService:

    def __init__(self):

        self.repository = MarketRepository()

    def get_history(self, filename="historical_data.csv"):

        return self.repository.history(filename)

    def get_prices(self, filename="historical_data.csv"):

        return self.repository.prices(filename)

    def get_last_symbol(self, filename="historical_data.csv"):

        return self.repository.symbol(filename)