
"""
Iran AI Trader Professional

Scanner V2

Sprint44-26

Price Score Engine - Shared Config Connected
"""

from scanner_v2.scoring.base_score import BaseScore


class PriceScoreEngine(BaseScore):

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


        start = prices[0]

        end = prices[-1]


        if start <= 0:

            return 0


        change = (

            (end - start)

            /

            start

        ) * 100


        score = 50 + change


        return self.clamp(
            score
        )

