"""
Iran AI Trader Professional

Scanner V2

Sprint44-17

History Loader Shared Config
"""

from scanner_v2.history_adapter import HistoryAdapter
from scanner_v2.config import ScannerConfig


class HistoryLoader:

    def __init__(
        self,
        adapter=None,
        config=None
    ):

        self.config = config or ScannerConfig()

        self.adapter = adapter or HistoryAdapter(
            config=self.config
        )

        self.failed_history = []


    def load(self, symbol):

        return self.load_history(symbol)


    def load_history(self, symbol):

        try:

            history = self.adapter.get_history(
                symbol
            )

            if history is None:

                raise Exception(
                    "No history returned"
                )

            return history


        except Exception as error:

            self.failed_history.append({

                "symbol": symbol,

                "error": str(error)

            })

            return None


    def validate_history(
        self,
        history,
        minimum_candles=None
    ):

        try:

            if history is None:

                return False

            prices = history.close_prices()

            if prices is None:

                return False

            if minimum_candles is None:

                minimum_candles = (
                    self.config.get_minimum_candles()
                )

            if len(prices) < minimum_candles:

                return False

            return True


        except Exception:

            return False


    def failed_count(self):

        return len(
            self.failed_history
        )

