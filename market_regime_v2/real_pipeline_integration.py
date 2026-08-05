"""
Iran AI Trader Professional

Real Pipeline Integration
Sprint41

Connects real_pipeline with Market Regime Hook V2
"""


from .real_pipeline_regime_hook_v2 import (
    RealPipelineRegimeHookV2
)



class RealPipelineIntegration:


    def __init__(self):

        self.regime_hook = RealPipelineRegimeHookV2()



    # -------------------------------------

    def market_check(

        self,

        market_data

    ):

        """
        Run market regime analysis before pipeline execution
        """


        return self.regime_hook.analyze(

            market_data

        )



    # -------------------------------------

    def stock_check(

        self,

        regime_result,

        stock_score

    ):

        """
        Check stock permission based on market regime
        """


        return self.regime_hook.evaluate_stock(

            regime_result["regime"],

            regime_result["score"],

            stock_score

        )



    # -------------------------------------

    def pipeline_status(self):

        """
        Integration status
        """


        return {

            "module": "RealPipelineIntegration",

            "regime_hook": self.regime_hook.status()

        }