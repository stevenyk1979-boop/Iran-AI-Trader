"""
Iran AI Trader Professional
Ranking Service
Sprint31-E
"""

from technical_analysis import TechnicalAnalysis
from multi_timeframe import MultiTimeFrameAnalyzer
from ai_score_engine import AIScoreEngine

from smart_money_integration import SmartMoneyIntegration


class RankingService:

    def __init__(self):

        self.ta = TechnicalAnalysis()

        self.mtf = MultiTimeFrameAnalyzer(
            self.ta
        )

        self.ai = AIScoreEngine()

        self.smart_money = SmartMoneyIntegration()

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

        # ----------------------------
        # Build initial result
        # ----------------------------

        result = {

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

        # ----------------------------------
        # Temporary Smart Money inputs
        # (later replaced with real values)
        # ----------------------------------

        result["volume_ratio"] = 1.0

        result["buyer_power"] = 1.0

        # ----------------------------------
        # Smart Money Integration
        # ----------------------------------

        result = self.smart_money.integrate(

            result

        )

        return result