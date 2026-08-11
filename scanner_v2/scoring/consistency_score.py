
"""
Iran AI Trader Professional

Scanner V2

Sprint44-26

Consistency Score Engine - Shared Config Connected
"""

from scanner_v2.scoring.base_score import BaseScore


class ConsistencyScoreEngine(BaseScore):

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

            change = (
                prices[index]
                -
                prices[index - 1]
            )


            if change > 0:

                increases += 1

            elif change < 0:

                decreases += 1


        total_directional_moves = (
            increases
            +
            decreases
        )


        if total_directional_moves == 0:

            return 50


        dominant_moves = max(
            increases,
            decreases
        )


        consistency = (

            dominant_moves
            /
            total_directional_moves

        ) * 100


        return self.clamp(
            consistency
        )

