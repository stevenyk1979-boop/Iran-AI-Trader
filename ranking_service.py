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

    # ---------------------------------

    def analyze(self, history, symbol=None):

        analysis = self.mtf.analyze_all(history)

        decision = self.ai.score(
            history,
            analysis,
            symbol
        )

        return decision