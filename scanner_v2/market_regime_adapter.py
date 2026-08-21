"""
Iran AI Trader Professional

Scanner V2

Market Regime Adapter

Connects Market Regime V2 to Scanner V2
without modifying RankingEngine.
"""

from market_regime_v2.market_regime_v2 import MarketRegimeV2


class MarketRegimeAdapter:

    def __init__(self, engine=None):

        self.engine = engine or MarketRegimeV2()


    def analyze(self, data):

        if data is None:

            return {
                "regime": "UNKNOWN",
                "score": 0
            }

        try:

            result = self.engine.calculate(data)

            if result is None:

                return {
                    "regime": "UNKNOWN",
                    "score": 0
                }

            return {
                "regime": result.get(
                    "regime",
                    "UNKNOWN"
                ),

                "score": result.get(
                    "score",
                    0
                ),

                "trend": result.get(
                    "trend",
                    0
                ),

                "breadth": result.get(
                    "breadth",
                    0
                ),

                "liquidity": result.get(
                    "liquidity",
                    0
                ),

                "volatility": result.get(
                    "volatility",
                    0
                ),

                "macro": result.get(
                    "macro",
                    0
                )
            }

        except Exception as error:

            return {
                "regime": "UNKNOWN",
                "score": 0,
                "error": str(error)
            }