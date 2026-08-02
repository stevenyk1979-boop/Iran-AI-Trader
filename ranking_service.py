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


    # ---------------------------------

    def analyze(

        self,

        history,

        symbol=None

    ):

        """
        Analyze one symbol history
        """


        analysis = self.mtf.analyze_all(

            history

        )


        result = self.ai.score(

            history,

            analysis,

            symbol

        )


        return {

            "symbol": symbol,

            "analysis": analysis,


            # Decision Result

            "detail": result.detail,

            "score": round(

                result.score,

                2

            ),

            "signal": result.signal,


            # New AI Information

            "confidence": result.confidence,

            "risk": result.risk,


            # Compatibility with Scanner

            "rsi": analysis["daily"].get(

                "rsi"

            ),

            "macd": analysis["daily"].get(

                "macd"

            ),

            "bollinger": analysis["daily"].get(

                "bollinger"

            )

        }