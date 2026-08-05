"""
Iran AI Trader Professional

Scanner V2

Sprint44-05

Validator Engine
"""


class Validator:


    def __init__(self):

        self.rejected = []



    def validate_history(
        self,
        history,
        symbol
    ):


        try:


            if history is None:

                raise Exception(
                    "History is None"
                )


            prices = history.close_prices()


            if prices is None:

                raise Exception(
                    "No prices"
                )


            if len(prices) < 20:

                raise Exception(
                    "Insufficient candles"
                )


            for price in prices:

                if price <= 0:

                    raise Exception(
                        "Invalid price"
                    )


            return True



        except Exception as error:


            self.rejected.append({

                "symbol": symbol,

                "reason": str(error)

            })


            return False




    def validate_score(
        self,
        score
    ):


        try:


            if score is None:

                return False



            if score < 0:

                return False



            if score > 100:

                return False



            return True



        except Exception:

            return False




    def rejected_count(self):

        return len(
            self.rejected
        )