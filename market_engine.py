"""
Iran AI Trader V2.0 Beta
Market Engine
"""

from market_cache import MarketCache
from download_manager import DownloadManager


class MarketEngine:

    def __init__(self):

        self.cache = MarketCache()

        self.downloader = DownloadManager()

        self.downloader.connect()

    def history(self, symbol):

        data = self.cache.load(symbol)

        if data is None:

            data = self.downloader.download_history(symbol)

            self.cache.save(symbol, data)

        return data

    def clear_cache(self):

        self.cache.clear()

    def cache_size(self):

        return self.cache.size()