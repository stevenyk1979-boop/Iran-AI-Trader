"""
Iran AI Trader V2.0 Beta
Download Manager
"""

from market_cache import MarketCache


class DownloadManager:

    def __init__(self):

        self.connected = False

        self.cache = MarketCache()

    def connect(self):

        self.connected = True

        return True

    def status(self):

        return self.connected

    def download_history(self, symbol):

        """
        نسخه آزمایشی

        بعداً داده واقعی TSETMC
        """

        prices = [

            100,
            101,
            102,
            103,
            104,
            106,
            108,
            107,
            110,
            112,
            113,
            115,
            117,
            118,
            120,
            122,
            121,
            123,
            124,
            126,
            128

        ]

        self.cache.save(symbol, prices)

        print(f"Downloading history for {symbol} ...")

        return prices

    def get_cached_history(self, symbol):

        return self.cache.load(symbol)