"""
Iran AI Trader Professional
Confidence Engine
"""


class ConfidenceEngine:

    def calculate(self, engines):

        """
        engines = {

            "trend": {...},

            "momentum": {...},

            "volume": {...},

            ...

        }

        """

        total = 0

        success = 0

        reasons = []

        for name, engine in engines.items():

            total += 1

            if engine["score"] > 0:

                success += 1

                reasons.append(f"{name}: OK")

            else:

                reasons.append(f"{name}: Weak")

        if total == 0:

            confidence = 0

        else:

            confidence = (

                success / total

            ) * 100

        return {

            "confidence": round(

                confidence,

                2

            ),

            "engines": success,

            "total": total,

            "reasons": reasons

        }