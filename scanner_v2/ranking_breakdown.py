
"""
Iran AI Trader Professional

Scanner V2

Sprint44-32

Ranking Breakdown
"""


class RankingBreakdown:

    def __init__(
        self,
        price_score,
        trend_score,
        price_weight,
        trend_weight
    ):

        self.price_score = price_score

        self.trend_score = trend_score

        self.price_weight = price_weight

        self.trend_weight = trend_weight


    def weight_sum(self):

        return (
            self.price_weight
            +
            self.trend_weight
        )


    def price_contribution(self):

        return (

            self.price_score
            *
            self.price_weight

        )


    def trend_contribution(self):

        return (

            self.trend_score
            *
            self.trend_weight

        )


    def final_score(self):

        total_weight = self.weight_sum()


        if total_weight <= 0:

            raise ValueError(
                "ranking weight sum must be > 0"
            )


        score = (

            self.price_contribution()
            +
            self.trend_contribution()

        ) / total_weight


        return round(
            score,
            2
        )


    def to_dict(self):

        return {

            "price": {

                "score": round(
                    self.price_score,
                    2
                ),

                "weight": self.price_weight,

                "contribution": round(
                    self.price_contribution(),
                    2
                )

            },

            "trend": {

                "score": round(
                    self.trend_score,
                    2
                ),

                "weight": self.trend_weight,

                "contribution": round(
                    self.trend_contribution(),
                    2
                )

            },

            "final_score": self.final_score()

        }

