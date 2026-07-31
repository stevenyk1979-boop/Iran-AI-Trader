"""
Iran AI Trader Professional
Trend Strength Engine
"""


class TrendStrength:

    def score(self, analysis):

        daily = analysis["daily"]

        score = 0

        reason = []

        sma = daily["sma"]
        ema = daily["ema"]
        close = daily["close"]

        if sma is None or ema is None:
            return {
                "score": 0,
                "reason": ["No moving averages"]
            }

        if close > ema:
            score += 10
            reason.append("Close > EMA")

        if ema > sma:
            score += 10
            reason.append("EMA > SMA")

        return {
            "score": score,
            "reason": reason
        }