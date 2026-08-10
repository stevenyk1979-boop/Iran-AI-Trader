"""
Iran AI Trader Professional

Scanner V2

Sprint44-16

History Adapter Config Connected
"""

from scanner_v2.config import ScannerConfig
from scanner_v2.fake_market_provider import FakeMarketProvider


class HistoryAdapter:

    def __init__(
        self,
        provider=None,
        config=None
    ):

        self.config = config or ScannerConfig()

        if provider is not None:

            self.provider = provider

        elif self.config.get_data_source() == "fake":

            self.provider = FakeMarketProvider()

        else:

            self.provider = None


    def get_history(self, symbol):

        try:

            if self.provider is None:

                return None

            return self.provider.get_history(
                symbol
            )

        except Exception:

            return None