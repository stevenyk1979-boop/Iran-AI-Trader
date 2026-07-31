"""
Iran AI Trader Professional
AI Score Engine
"""


class AIScoreEngine:

    def score(self, analysis):

        score = 0

        detail = {}

        daily = analysis["daily"]


        # Trend

        trend = 0

        if daily["ema"] > daily["sma"]:

            trend = 20

        detail["trend"] = trend

        score += trend


        # Momentum

        momentum = 0

        if daily["rsi"] is not None:

            if 45 <= daily["rsi"] <= 70:

                momentum = 20

        detail["momentum"] = momentum

        score += momentum


        # MACD

        macd_score = 0

        if daily["macd"] is not None:

            macd_score = 20

        detail["macd"] = macd_score

        score += macd_score


        # Bollinger

        bollinger_score = 0

        if daily["bollinger"] is not None:

            bollinger_score = 20

        detail["bollinger"] = bollinger_score

        score += bollinger_score


        # Risk

        risk = 20

        detail["risk"] = risk

        score += risk


        if score >= 85:

            signal = "STRONG BUY"

        elif score >= 70:

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