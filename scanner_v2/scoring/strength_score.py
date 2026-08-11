
"""
Iran AI Trader Professional

Scanner V2

Sprint44-26

Strength Score Engine - Shared Config Connected
"""

from scanner_v2.scoring.base_score import BaseScore


class StrengthScoreEngine(BaseScore):

    def __init__(self, config=None):

        self.config = config


    def calculate(
        self,
        prices
    ):

        if prices is None:

            return 0


        if len(prices) < 2:

            return 0


        average_price = (
            sum(prices)
            /
            len(prices)
        )


        if average_price <= 0:

            return 0


        average_move = sum(

            abs(
                prices[index]
                -
                prices[index - 1]
            )

            for index in range(
                1,
                len(prices)
            )

        ) / (len(prices) - 1)


        strength_percent = (

            average_move
            /
            average_price

        ) * 100


        score = strength_percent * 100


        return self.clamp(
            score
        )

