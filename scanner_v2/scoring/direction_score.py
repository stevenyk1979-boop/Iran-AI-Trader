
"""
Iran AI Trader Professional

Scanner V2

Sprint44-26

Direction Score Engine - Shared Config Connected
"""

from scanner_v2.scoring.base_score import BaseScore


class DirectionScoreEngine(BaseScore):

    def __init__(self, config=None):

        self.config = config


    def calculate(
        self,
        prices
    ):

        if prices is None:

            return 50


        if len(prices) < 2:

            return 50


        increases = 0

        decreases = 0


        for index in range(
            1,
            len(prices)
        ):

            if prices[index] > prices[index - 1]:

                increases += 1

            elif prices[index] < prices[index - 1]:

                decreases += 1


        total_directional_moves = (
            increases
            +
            decreases
        )


        if total_directional_moves == 0:

            return 50


        direction_ratio = (

            increases

            /

            total_directional_moves

        )


        score = direction_ratio * 100


        return self.clamp(
            score
        )

