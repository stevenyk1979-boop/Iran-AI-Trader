"""
Iran AI Trader Professional

Real Pipeline Regime Adapter
Sprint40

Bridge between Real Pipeline and Market Regime V2
"""


from .pipeline_regime_controller import PipelineRegimeController

from .scanner_regime_bridge import ScannerRegimeBridge



class RealPipelineRegimeAdapter:


    def __init__(self):

        self.controller = PipelineRegimeController()

        self.scanner_bridge = ScannerRegimeBridge()



    # -------------------------------------

    def analyze_market(

        self,

        regime_data

    ):

        """
        Analyze market regime from pipeline
        """


        result = self.controller.evaluate(

            regime_data

        )


        return result



    # -------------------------------------

    def evaluate_stock(

        self,

        regime,

        market_score,

        stock_score

    ):

        """
        Evaluate stock opportunity
        """


        result = self.scanner_bridge.evaluate(

            regime,

            market_score,

            stock_score

        )


        return result