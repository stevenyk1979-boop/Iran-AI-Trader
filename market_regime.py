"""
Iran AI Trader Professional
Market Regime Engine
Sprint30-A
"""

from regime_config import *


class MarketRegimeEngine:

    def __init__(self):

        pass

    # ----------------------------

    def calculate(

        self,

        ranking

    ):

        if len(ranking) == 0:

            return {

                "regime": "UNKNOWN",

                "score": 0,

                "confidence": 0

            }

        average = sum(

            x["score"]

            for x in ranking

        ) / len(ranking)

        if average >= BULL_THRESHOLD:

            regime = "BULL"

        elif average >= SIDEWAYS_THRESHOLD:

            regime = "SIDEWAYS"

        else:

            regime = "BEAR"

        return {

            "regime": regime,

            "score": round(

                average,

                2

            ),

            "confidence": MARKET_CONFIDENCE

        }