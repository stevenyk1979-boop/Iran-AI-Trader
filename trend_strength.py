"""
Iran AI Trader Professional
Trend Strength Engine
"""


class TrendStrength:

    MAX_SCORE = 20

    def score(self, analysis):

        daily = analysis["daily"]

        score = 0

        reason = []

        sma = daily.get("sma")

        ema = daily.get("ema")

        close = daily.get("close")


        if sma is None or ema is None or close is None:

            return {

                "score": 0,

                "max_score": self.MAX_SCORE,

                "reason": [

                    "No moving averages"

                ]

            }


        if close > ema:

            score += 10

            reason.append(

                "Close > EMA"

            )


        if ema > sma:

            score += 10

            reason.append(

                "EMA > SMA"

            )


        return {

            "score": score,

            "max_score": self.MAX_SCORE,

            "reason": reason

        }