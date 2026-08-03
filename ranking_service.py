"""
Iran AI Trader Professional
Ranking Service
"""

from technical_analysis import TechnicalAnalysis
from multi_timeframe import MultiTimeFrameAnalyzer
from ai_score_engine import AIScoreEngine


class RankingService:

    def __init__(self):

        self.ta = TechnicalAnalysis()

        self.mtf = MultiTimeFrameAnalyzer(
            self.ta
        )

        self.ai = AIScoreEngine()


    # -------------------------------------

    def analyze(

        self,

        history,

        symbol=None

    ):

        """
        Analyze one symbol history
        """


        # Multi timeframe analysis

        analysis = self.mtf.analyze_all(

            history

        )


        # AI Decision Engine

        decision = self.ai.score(

            history,

            analysis,

            symbol

        )


        # DecisionResult -> Dictionary

        return {

            "symbol": symbol,


            "analysis": analysis,


            "detail": decision.detail,


            "score": round(

                decision.score,

                2

            ),


            "signal": decision.signal,


            "confidence": decision.confidence,


            "risk": decision.risk,


            # Compatibility with Scanner

            "rsi": analysis.get(

                "daily",

                {}

            ).get(

                "rsi"

            ),


            "macd": analysis.get(

                "daily",

                {}

            ).get(

                "macd"

            ),


            "bollinger": analysis.get(

                "daily",

                {}

            ).get(

                "bollinger"

            )

        }