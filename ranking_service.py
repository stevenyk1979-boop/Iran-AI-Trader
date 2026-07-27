"""
Iran AI Trader V2.0
Ranking Service
"""

from technical_analysis import TechnicalAnalysis
from score_engine import ScoreEngine


class RankingService:

    def __init__(self):

        self.ta = TechnicalAnalysis()
        self.engine = ScoreEngine()

    def analyze(self, prices):

        rsi = self.ta.rsi(prices)

        macd = self.ta.macd(prices)

        bands = self.ta.bollinger(prices)

        score = self.engine.total_score(
            rsi,
            macd,
            bands,
            prices[-1]
        )

        signal = self.engine.recommendation(score)

        return {

            "rsi": rsi,

            "macd": macd,

            "bollinger": bands,

            "score": score,

            "signal": signal

        }