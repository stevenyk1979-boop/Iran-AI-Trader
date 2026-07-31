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

        self.mtf = MultiTimeFrameAnalyzer(self.ta)

        self.ai = AIScoreEngine()

    def analyze(self, history):

        """
        Analyze one symbol history
        """

        analysis = self.mtf.analyze_all(history)

        result = self.ai.score(analysis)

        return {

            "analysis": analysis,

            "detail": result["detail"],

            "score": result["score"],

            "signal": result["signal"],

            # برای سازگاری با نسخه فعلی Scanner
            "rsi": analysis["daily"]["rsi"],

            "macd": analysis["daily"]["macd"],

            "bollinger": analysis["daily"]["bollinger"]

        }