"""
Iran AI Trader V2.0 Beta
Market Service
"""

from market_repository import MarketRepository
from download_manager import DownloadManager


class MarketService:

    def __init__(self):

        self.repository = MarketRepository()

        self.downloader = DownloadManager()

        self.downloader.connect()

    def get_history(self, filename="historical_data.csv"):

        return self.repository.history(filename)

    def get_prices(self, filename="historical_data.csv"):

        return self.repository.prices(filename)

    def get_last_symbol(self, filename="historical_data.csv"):

        return self.repository.symbol(filename)

    def get_live_prices(self, symbol):

        cached = self.downloader.get_cached_history(symbol)

        if cached is not None:

            return cached

        return self.downloader.download_history(symbol)