"""
Iran AI Trader Professional
Momentum Engine
"""


class MomentumEngine:

    MAX_SCORE = 20

    def score(self, analysis):

        daily = analysis["daily"]

        rsi = daily.get("rsi")

        score = 0

        reason = []


        if rsi is None:

            return {

                "score": 0,

                "max_score": self.MAX_SCORE,

                "reason": [

                    "No RSI"

                ]

            }


        if 45 <= rsi <= 70:

            score = 20

            reason.append(

                "Healthy RSI"

            )


        elif 35 <= rsi < 45:

            score = 10

            reason.append(

                "Recovering RSI"

            )


        elif 70 < rsi <= 80:

            score = 10

            reason.append(

                "Strong but overbought"

            )


        else:

            reason.append(

                "Weak Momentum"

            )


        return {

            "score": score,

            "max_score": self.MAX_SCORE,

            "reason": reason

        }