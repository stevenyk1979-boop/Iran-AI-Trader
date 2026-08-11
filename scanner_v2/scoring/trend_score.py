
"""
Iran AI Trader Professional

Scanner V2

Sprint44-26

Trend Score Engine - Shared Config Connected
"""

from scanner_v2.scoring.base_score import BaseScore


class TrendScoreEngine(BaseScore):

    def __init__(self, config=None):

        self.config = config


    def calculate(
        self,
        direction_score,
        strength_score,
        consistency_score
    ):

        if direction_score is None:

            direction_score = 50


        if strength_score is None:

            strength_score = 0


        if consistency_score is None:

            consistency_score = 50


        score = (

            (direction_score * 0.40)

            +

            (strength_score * 0.30)

            +

            (consistency_score * 0.30)

        )


        return self.clamp(
            score
        )

