"""
Iran AI Trader Professional
Position Sizer
Sprint32-B
"""


class PositionSizer:

    def __init__(self):
        pass

    # ---------------------------------------

    def calculate(

        self,

        capital,

        price

    ):

        """
        Calculate number of shares
        """

        if price <= 0:

            return {

                "shares": 0,

                "capital_used": 0

            }

        shares = int(

            capital / price

        )

        capital_used = round(

            shares * price,

            2

        )

        return {

            "shares": shares,

            "capital_used": capital_used

        }