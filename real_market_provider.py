"""
Iran AI Trader Professional
Real Market Provider
"""

from real_market_adapter import RealMarketAdapter
from runtime_config import (
    TEST_MODE,
    TEST_SYMBOL_COUNT
)


class RealMarketProvider:

    def __init__(self):

        self.adapter = RealMarketAdapter()

    # -------------------------------------

    def get_symbols(self):

        symbols = self.adapter.symbols()

        if TEST_MODE:

            return symbols[:TEST_SYMBOL_COUNT]

        return symbols

    # -------------------------------------

    def get_history(

        self,

        symbol,

        days=100

    ):

        return self.adapter.history(

            symbol,

            days

        )

    # -------------------------------------

    def is_available(self):

        return self.adapter.status()