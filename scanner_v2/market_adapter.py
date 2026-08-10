"""
Iran AI Trader Professional

Scanner V2

Sprint44-15

Market Adapter Config Connected
"""

from scanner_v2.config import ScannerConfig
from scanner_v2.fake_market_provider import FakeMarketProvider


class MarketAdapter:

    def __init__(self, provider=None, config=None):

        self.config = config or ScannerConfig()

        if provider is not None:

            self.provider = provider

        elif self.config.get_data_source() == "fake":

            self.provider = FakeMarketProvider()

        else:

            self.provider = None


    def get_symbols(self):

        try:

            if self.provider is None:

                return []

            return self.provider.get_symbols()

        except Exception:

            return []


    def get_history(self, symbol):

        try:

            if self.provider is None:

                return None

            return self.provider.get_history(

                symbol

            )

        except Exception:

            return None