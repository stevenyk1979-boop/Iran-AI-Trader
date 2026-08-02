"""
Iran AI Trader Professional
Market Service
"""

from provider_factory import ProviderFactory


class MarketService:

    def __init__(self):

        self.provider = ProviderFactory.create()

    def symbols(self):

        return self.provider.get_symbols()

    def get_prices(self, filename):

        return self.provider.get_prices(filename)

    def history(self, symbol):

        if hasattr(self.provider, "get_history"):

            return self.provider.get_history(symbol)

        return None

    def available(self):

        if hasattr(self.provider, "is_available"):

            return self.provider.is_available()

        return False