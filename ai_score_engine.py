"""
Iran AI Trader Professional
AI Score Engine
"""

from trend_strength import TrendStrength
from momentum_engine import MomentumEngine


class AIScoreEngine:

    def __init__(self):

        self.trend = TrendStrength()
        self.momentum = MomentumEngine()

    def score(self, analysis):

        score = 0

        detail = {}

        # ---------------------------------
        # Trend
        # ---------------------------------

        trend = self.trend.score(analysis)

        score += trend["score"]

        detail["trend"] = trend

        # ---------------------------------
        # Momentum
        # ---------------------------------

        momentum = self.momentum.score(analysis)

        score += momentum["score"]

        detail["momentum"] = momentum

        # ---------------------------------
        # MACD
        # ---------------------------------

        macd_score = 0

        daily = analysis["daily"]

        macd = daily.get("macd")

        if macd is not None:

            macd_score = 20

        score += macd_score

        detail["macd"] = {

            "score": macd_score,

            "value": macd

        }

        # ---------------------------------
        # Bollinger
        # ---------------------------------

        boll_score = 0

        bands = daily.get("bollinger")

        if bands is not None:

            boll_score = 20

        score += boll_score

        detail["bollinger"] = {

            "score": boll_score,

            "value": bands

        }

        # ---------------------------------
        # Risk
        # ---------------------------------

        risk_score = 20

        score += risk_score

        detail["risk"] = risk_score

        # ---------------------------------
        # Final Decision
        # ---------------------------------

        if score >= 90:

            signal = "STRONG BUY"

        elif score >= 75:

            signal = "BUY"

        elif score >= 50:

            signal = "HOLD"

        else:

            signal = "SELL"

        return {

            "score": score,

            "signal": signal,

            "detail": detail

        }