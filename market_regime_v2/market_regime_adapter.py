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

    def analyze(self, market_data):

        """
        Safe adapter interface
        """

        try:


            result = self.engine.calculate(

                market_data

            )


            return {


                "success": True,


                "regime": result["regime"],


                "score": result["score"],


                "trend": result["trend"],


                "breadth": result["breadth"],


                "liquidity": result["liquidity"],


                "volatility": result["volatility"],


                "macro": result["macro"]

            }



        except Exception as e:


            return {


                "success": False,


                "regime": "UNKNOWN",


                "score": 0,


                "error": str(e)

            }