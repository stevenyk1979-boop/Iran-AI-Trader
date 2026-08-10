"""
Iran AI Trader Professional

Scanner V2

Sprint44-14

History Loader Adapter Connected
"""


from scanner_v2.history_adapter import HistoryAdapter


class HistoryLoader:


    def __init__(self, adapter=None):

        self.adapter = adapter or HistoryAdapter()

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
        minimum_candles=20
    ):

        try:

            if history is None:

                return False


            prices = history.close_prices()


            if prices is None:

                return False


            if len(prices) < minimum_candles:

                return False


            return True


        except Exception:

            return False


    def failed_count(self):

        return len(

            self.failed_history

        )