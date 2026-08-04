"""
Iran AI Trader Professional
Portfolio Optimizer
Sprint33-A
"""


from portfolio_config import (
    MAX_POSITIONS,
    MAX_SECTOR_EXPOSURE,
    MIN_SCORE
)



class PortfolioOptimizer:


    def __init__(self):

        pass



    # -------------------------------------

    def filter_quality(

        self,

        decisions

    ):


        return [

            item

            for item in decisions

            if item.get(

                "score",

                0

            ) >= MIN_SCORE

        ]



    # -------------------------------------

    def limit_positions(

        self,

        decisions

    ):


        ranked = sorted(

            decisions,

            key=lambda x: x.get(

                "score",

                0

            ),

            reverse=True

        )


        return ranked[:MAX_POSITIONS]



    # -------------------------------------

    def optimize(

        self,

        decisions

    ):

        """

        Create optimized portfolio

        """


        quality = self.filter_quality(

            decisions

        )


        portfolio = self.limit_positions(

            quality

        )


        return {


            "total_candidates":

                len(decisions),


            "quality_candidates":

                len(quality),


            "selected":

                portfolio

        }