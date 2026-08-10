"""
Iran AI Trader Professional

Scanner V2

Sprint44-13

History Adapter
"""


from scanner_v2.fake_market_provider import FakeMarketProvider


class HistoryAdapter:


    def __init__(self, provider=None):

        if provider is None:

            provider = FakeMarketProvider()

        self.provider = provider


    def get_history(self, symbol):

        try:

            return self.provider.get_history(

                symbol

            )

        except Exception:

            return None