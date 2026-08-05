"""
Iran AI Trader Professional

Real Pipeline Runtime Bridge
Sprint42.5

Bridge layer between
Real Pipeline and Runtime Hook
"""


from .real_pipeline_runtime_hook import (
    RealPipelineRuntimeHook
)



class RealPipelineRuntimeBridge:


    def __init__(self):

        self.runtime_hook = RealPipelineRuntimeHook()

        self.mode = "SHADOW"



    # -------------------------------------

    def check_market(

        self,

        market_data

    ):

        """
        Execute runtime market validation
        """


        result = self.runtime_hook.pre_scan_check(

            market_data

        )


        return {

            "success": result["success"],

            "allowed": result["allowed"],

            "mode": self.mode,

            "regime": result.get("regime", "UNKNOWN"),

            "score": result.get("score", 0),

            "message": result.get(

                "message",

                ""

            )

        }



    # -------------------------------------

    def check_stock(

        self,

        market_result,

        stock_score

    ):

        """
        Execute stock validation
        """


        return self.runtime_hook.stock_check(

            market_result,

            stock_score

        )



    # -------------------------------------

    def status(self):

        """
        Bridge status
        """


        return {

            "module": "RealPipelineRuntimeBridge",

            "mode": self.mode,

            "hook": self.runtime_hook.status()

        }