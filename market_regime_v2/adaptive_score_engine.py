"""
Iran AI Trader Professional

Adaptive Score Engine
Sprint38.5

Regime aware scoring system
"""


from .regime_weight_engine import RegimeWeightEngine



class AdaptiveScoreEngine:


    def __init__(self):

        self.weight_engine = RegimeWeightEngine()



    # -------------------------------------

    def calculate(

        self,

        regime,

        technical_score,

        momentum_score,

        liquidity_score,

        risk_score

    ):

        """
        Calculate adaptive stock score
        based on market regime
        """


        weights = self.weight_engine.get_weights(

            regime

        )


        final_score = (

            technical_score * weights["technical"]

            +

            momentum_score * weights["momentum"]

            +

            liquidity_score * weights["liquidity"]

            +

            risk_score * weights["risk"]

        )


        # Normalize

        final_score = final_score / (

            weights["technical"]

            +

            weights["momentum"]

            +

            weights["liquidity"]

            +

            weights["risk"]

        )


        if final_score > 100:

            final_score = 100


        if final_score < 0:

            final_score = 0



        return {


            "regime": regime,


            "score": round(

                final_score,

                2

            ),


            "weights": weights

        }