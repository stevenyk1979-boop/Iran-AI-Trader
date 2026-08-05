"""
Iran AI Trader Professional
Pipeline Regime Bridge
Sprint37
"""


from .market_regime_adapter import MarketRegimeAdapter



class PipelineRegimeBridge:


    def __init__(self):

        self.adapter = MarketRegimeAdapter()



    # -------------------------------------

    def analyze_market(self, market_data):

        """

        Send data to Market Regime Adapter

        """


        return self.adapter.analyze(

            market_data

        )



    # -------------------------------------

    def trading_permission(self, result):

        """

        Trading permission logic

        """


        if not result.get(

            "success",

            False

        ):

            return {


                "allowed": False,

                "mode": "ERROR"

            }



        regime = result.get(

            "regime",

            "UNKNOWN"

        )


        if regime in [


            "STRONG BULL",

            "BULL"

        ]:


            return {


                "allowed": True,

                "mode": "NORMAL"

            }



        elif regime == "EARLY BULL":


            return {


                "allowed": True,

                "mode": "CAUTIOUS"

            }



        elif regime == "SIDEWAYS":


            return {


                "allowed": False,

                "mode": "SELECTIVE"

            }



        else:


            return {


                "allowed": False,

                "mode": "CAPITAL PROTECTION"

            }



    # -------------------------------------

    def evaluate(self, market_data):


        regime_result = self.analyze_market(

            market_data

        )


        permission = self.trading_permission(

            regime_result

        )


        return {


            "regime": regime_result,

            "permission": permission

        }