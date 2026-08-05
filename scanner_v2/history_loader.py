"""
Iran AI Trader Professional

Scanner V2

Sprint44-03

History Loader
"""


class HistoryLoader:


    def __init__(self, market_service=None):

        self.market_service = market_service

        self.failed_history = []



    def load_history(self, symbol):

        try:

            if self.market_service is None:

                raise Exception(
                    "Market service not configured"
                )


            history = self.market_service.history(

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