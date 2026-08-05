"""
Iran AI Trader Professional
Market Regime Adapter
Sprint37
"""


from .market_regime_v2 import MarketRegimeV2



class MarketRegimeAdapter:


    def __init__(self):

        self.engine = MarketRegimeV2()



    # -------------------------------------

    def analyze(self, data):

        """

        Adapter interface

        """


        try:


            result = self.engine.calculate(

                data

            )


            result["success"] = True


            return result



        except Exception as e:


            return {


                "success": False,

                "error": str(e),

                "regime": "UNKNOWN",

                "score": 0

            }