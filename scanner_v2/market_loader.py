
"""
Iran AI Trader Professional

Scanner V2

Sprint44-18

Market Loader Shared Config
"""

from scanner_v2.market_adapter import MarketAdapter
from scanner_v2.config import ScannerConfig


class MarketLoader:

    def __init__(
        self,
        adapter=None,
        config=None
    ):

        self.config = config or ScannerConfig()

        self.adapter = adapter or MarketAdapter(
            config=self.config
        )

        self.symbols = []


    def load_symbols(self, data=None):

        try:

            if data is None:

                data = self.adapter.get_symbols()


            result = []


            for item in data:

                if item is None:

                    continue


                if isinstance(item, dict):

                    symbol = item.get(
                        "symbol"
                    )

                else:

                    symbol = item


                if not symbol:

                    continue


                result.append(
                    symbol
                )


            self.symbols = result

            return result


        except Exception:

            self.symbols = []

            return []


    def count(self):

        return len(
            self.symbols
        )

