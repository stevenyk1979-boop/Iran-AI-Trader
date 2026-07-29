"""
Iran AI Trader Professional
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

        ranking = []

        symbols = self.market.symbols()

        if not symbols:

            print("Market is empty.")

            return []

        for item in symbols:

            symbol = item["symbol"]

            filename = item["file"]

            prices = self.market_service.get_prices(filename)

            if not prices:

                continue

            result = self.ranking_service.analyze(prices)

            ranking.append({

                "symbol": symbol,

                "score": result["score"],

                "signal": result["signal"],

                "price": prices[-1],

                "rsi": result["rsi"],

                "macd": result["macd"],

                "bollinger": result["bollinger"]

            })

        ranking.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        return ranking