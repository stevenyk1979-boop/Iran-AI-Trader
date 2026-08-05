"""
Iran AI Trader Professional

Real Pipeline Runtime Hook
Sprint42

Runtime control layer between
Real Pipeline and Market Regime System
"""


from .real_pipeline_integration import (
    RealPipelineIntegration
)



class RealPipelineRuntimeHook:


    def __init__(self):

        self.integration = RealPipelineIntegration()

        self.enabled = True



    # -------------------------------------

    def pre_scan_check(

        self,

        market_data

    ):

        """
        Check market condition before scanner execution
        """


        if not self.enabled:

            return {

                "success": False,

                "allowed": False,

                "reason": "Runtime hook disabled"

            }



        result = self.integration.market_check(

            market_data

        )



        if not result["success"]:

            return {

                "success": False,

                "allowed": False,

                "reason": "Market analysis failed"

            }



        return {

            "success": True,

            "allowed": True,

            "regime": result["regime"],

            "score": result["score"],

            "message": "Market condition accepted"

        }



    # -------------------------------------

    def stock_check(

        self,

        regime_result,

        stock_score

    ):

        """
        Check individual stock permission
        """


        return self.integration.stock_check(

            regime_result,

            stock_score

        )



    # -------------------------------------

    def status(self):

        """
        Runtime hook status
        """


        return {

            "enabled": self.enabled,

            "module": "RealPipelineRuntimeHook"

        }