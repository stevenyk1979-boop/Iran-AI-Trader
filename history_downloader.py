"""
Iran AI Trader Professional
History Downloader V2
"""

from datetime import datetime, timedelta

from market_cache import MarketCache
from tsetmc_history import TSETMCHistory


class HistoryDownloader:

    CACHE_EXPIRE_HOURS = 12

    def __init__(self):

        self.cache = MarketCache()

        self.provider = TSETMCHistory()

    def _cache_expired(self, symbol):

        info = self.cache.info(symbol)

        if not info:

            return True

        updated = info.get("updated")

        if not updated:

            return True

        try:

            updated_time = datetime.strptime(
                updated,
                "%Y-%m-%d %H:%M:%S"
            )

        except Exception:

            return True

        age = datetime.now() - updated_time

        return age > timedelta(
            hours=self.CACHE_EXPIRE_HOURS
        )

    def get_history(self, symbol, days=30):

        """
        Return history using smart cache
        """

        if self.cache.exists(symbol):

            if not self._cache_expired(symbol):

                return self.cache.load(symbol)

        history = self.provider.get_history(

            symbol,

            days

        )

        self.cache.save(

            symbol,

            history

        )

        return history

    def update(self, symbol, days=30):

        history = self.provider.get_history(

            symbol,

            days

        )

        self.cache.save(

            symbol,

            history

        )

        return history

    def clear(self):

        self.cache.clear()

    def info(self, symbol):

        return self.cache.info(symbol)