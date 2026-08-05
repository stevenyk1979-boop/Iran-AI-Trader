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
    # Analyze Market State
    # -------------------------------------

    def analyze_market(self, market_data):

        """
        Connect Pipeline data to Market Regime V2
        """


        result = self.adapter.analyze(

            market_data

        )


        return result



    # -------------------------------------
    # Trading Permission
    # -------------------------------------

    def trading_permission(self, result):

        """
        Decide if aggressive trading is allowed
        """


        if not result.get("success"):

            return {


                "allowed": False,


                "reason": "REGIME ENGINE ERROR"

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
    # Full Pipeline Decision
    # -------------------------------------

    def evaluate(self, market_data):

        """
        Final bridge output
        """


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