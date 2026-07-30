"""
Iran AI Trader Professional
History Downloader
"""

from market_cache import MarketCache
from tsetmc_connector import TSETMCConnector
from tsetmc_history import TSETMCHistory


class HistoryDownloader:

    def __init__(self):

        self.cache = MarketCache()

        self.connector = TSETMCConnector()

        self.history = TSETMCHistory(
            self.connector
        )

    def download(self, symbol):

        if self.cache.exists(symbol):

            return self.cache.filename(symbol)

        csv_text = self.history.download_csv(symbol)

        self.cache.save(
            symbol,
            csv_text
        )

        return self.cache.filename(symbol)

    def update(self, symbol):

        csv_text = self.history.download_csv(symbol)

        self.cache.save(
            symbol,
            csv_text
        )

        return self.cache.filename(symbol)

    def update_all(self, symbols):

        for symbol in symbols:

            self.update(symbol)