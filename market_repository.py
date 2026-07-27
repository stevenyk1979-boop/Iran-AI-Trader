"""
Iran AI Trader V2.0 Alpha
Market Repository
"""

from data_provider import DataProvider


class MarketRepository:

    def __init__(self):

        self.provider = DataProvider()

    def history(self, filename="historical_data.csv"):

        return self.provider.load_history(filename)

    def prices(self, filename="historical_data.csv"):

        return self.provider.get_prices(filename)

    def symbol(self, filename="historical_data.csv"):

        return self.provider.get_symbol(filename)