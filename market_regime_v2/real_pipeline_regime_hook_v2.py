"""
Iran AI Trader Professional

Real Pipeline Regime Hook V2
Sprint40.5

Final connection layer between
Real Pipeline and Market Regime System
"""


from .real_pipeline_regime_adapter import (
    RealPipelineRegimeAdapter
)



class RealPipelineRegimeHookV2:


    def __init__(self):

        self.adapter = RealPipelineRegimeAdapter()

        self.active = True



    # -------------------------------------

    def analyze(

        self,

        market_data

    ):

        """
        Analyze market state
        """


        if not self.active:

            return {

                "success": False,

                "error": "Hook disabled"

            }



        result = self.adapter.analyze_market(

            market_data

        )



        # Handle nested adapter response

        if "regime" in result and isinstance(result["regime"], dict):

            result = result["regime"]



        return {

            "success": True,

            "active": True,

            "regime": result["regime"],

            "score": result["score"],

            "trend": result["trend"],

            "breadth": result["breadth"],

            "liquidity": result["liquidity"],

            "volatility": result["volatility"],

            "macro": result["macro"]

        }



    # -------------------------------------

    def evaluate_stock(

        self,

        regime,

        market_score,

        stock_score

    ):

        """
        Evaluate scanner opportunity
        """


        return self.adapter.evaluate_stock(

            regime,

            market_score,

            stock_score

        )



    # -------------------------------------

    def status(self):

        """
        Hook status
        """


        return {

            "active": self.active,

            "module": "RealPipelineRegimeHookV2"

        }