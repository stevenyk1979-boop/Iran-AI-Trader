"""
Iran AI Trader V2.0 Alpha
Scanner Engine
"""

from market_service import MarketService
from ranking_service import RankingService
from sample_market import SampleMarket


class Scanner:

    def __init__(self):

        self.market = SampleMarket()

        self.market_service = MarketService()

        self.ranking_service = RankingService()

    def scan(self):

        print()
        print("=" * 60)
        print("Scanner Report")
        print("=" * 60)

        ranking = []

        symbols = self.market.symbols()

        for item in symbols:

            symbol = item["symbol"]

            filename = item["file"]

            history = self.market_service.get_history(filename)

            prices = self.market_service.get_prices(filename)

            result = self.ranking_service.analyze(prices)

            ranking.append(
                (
                    symbol,
                    result["score"],
                    result["signal"],
                    prices[-1],
                    result["rsi"],
                    result["macd"],
                    result["bollinger"]
                )
            )

        ranking.sort(
            key=lambda x: x[1],
            reverse=True
        )

        print()

        print(
            f"{'Symbol':<12}"
            f"{'Score':>8}"
            f"{'Signal':>18}"
        )

        print("-" * 42)

        for row in ranking:

            print(
                f"{row[0]:<12}"
                f"{row[1]:>8}"
                f"{row[2]:>18}"
            )

        print()

        print("=" * 60)
        print("Top Symbol Details")
        print("=" * 60)

        best = ranking[0]

        print("Symbol     :", best[0])
        print("Last Price :", best[3])
        print("RSI        :", best[4])
        print("MACD       :", best[5])
        print("Bollinger  :", best[6])