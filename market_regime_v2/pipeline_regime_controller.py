"""
Iran AI Trader Professional
Pipeline Regime Controller
Sprint38
"""


from .pipeline_regime_bridge import PipelineRegimeBridge

from . import pipeline_regime_config as config



class PipelineRegimeController:


    def __init__(self):

        self.bridge = PipelineRegimeBridge()



    # -------------------------------------

    def evaluate(self, market_data):

        """
        Central control point for Market Regime
        """


        if not config.ENABLE_MARKET_REGIME_V2:

            return {

                "active": False,

                "mode": "LEGACY",

                "regime": {

                    "regime": config.DEFAULT_REGIME,

                    "score": 0

                },

                "permission": {

                    "allowed": False,

                    "mode": "LEGACY"

                }

            }



        result = self.bridge.evaluate(

            market_data

        )


        return {

            "active": True,

            "mode": config.REGIME_MODE,

            "regime": result["regime"],

            "permission": result["permission"]

        }



    # -------------------------------------

    def can_trade(self, result):

        """

        Trading permission check
        """


        return result.get(

            "permission",

            {}

        ).get(

            "allowed",

            False

        )



    # -------------------------------------

    def summary(self, result):

        """

        Compact summary

        """


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


            "trade_allowed": self.can_trade(

                result

            )

        }