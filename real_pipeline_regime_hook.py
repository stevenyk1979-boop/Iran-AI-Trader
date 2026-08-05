"""
Iran AI Trader Professional
Real Pipeline Regime Hook
Sprint38
"""


from market_regime_v2.pipeline_regime_controller import (
    PipelineRegimeController
)



class RealPipelineRegimeHook:


    def __init__(self):

        self.controller = PipelineRegimeController()



    # -------------------------------------

    def analyze(self, market_data):

        return self.controller.evaluate(

            market_data

        )



    # -------------------------------------

    def allow_trade(self, result):

        return self.controller.can_trade(

            result

        )



    # -------------------------------------

    def summary(self, result):


        return {


            "active": result.get(

                "active",

                False

            ),


            "mode": result.get(

                "mode",

                "UNKNOWN"

            ),


            "regime": result["regime"].get(

                "regime",

                "UNKNOWN"

            ),


            "score": result["regime"].get(

                "score",

                0

            ),


            "trade_allowed": result["permission"].get(

                "allowed",

                False

            )

        }