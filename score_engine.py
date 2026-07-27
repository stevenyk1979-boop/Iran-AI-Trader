"""
Iran AI Trader V2.0
Score Engine
"""


class ScoreEngine:

    def __init__(self):

        self.score = 0

    def score_rsi(self, rsi):

        if rsi is None:
            return 0

        if rsi < 30:
            return 20

        if rsi < 40:
            return 15

        if rsi < 50:
            return 10

        return 5

    def score_macd(self, macd):

        if macd is None:
            return 0

        if macd > 0:
            return 20

        return 5

    def score_bollinger(self, bands, price):

        if bands is None:
            return 0

        lower, middle, upper = bands

        if price <= lower:
            return 20

        if price <= middle:
            return 10

        return 5

    def total_score(
        self,
        rsi,
        macd,
        bands,
        price,
    ):

        score = 0

        score += self.score_rsi(rsi)

        score += self.score_macd(macd)

        score += self.score_bollinger(
            bands,
            price
        )

        return score

    def recommendation(self, score):

        if score >= 50:
            return "STRONG BUY"

        if score >= 35:
            return "BUY"

        if score >= 20:
            return "HOLD"

        return "SELL"