"""
Iran AI Trader Professional
Scanner Engine
"""

from market_service import MarketService
from ranking_service import RankingService


class Scanner:

    def __init__(self):

        self.market_service = MarketService()

        self.ranking_service = RankingService()

    def scan(self):

        ranking = []

        symbols = self.market_service.symbols()

        for item in symbols:

            symbol = item["symbol"]

            try:

                history = self.market_service.history(symbol)

            except Exception as error:

                print(f"Skip {symbol} - {error}")

                continue

            if history is None:

                continue

            try:

                prices = history.close_prices()

            except Exception:

                continue

            if len(prices) < 20:

                continue

            result = self.ranking_service.analyze(history)

            ranking.append({

                "symbol": symbol,

                "score": result["score"],

                "signal": result["signal"],

                "price": prices[-1],

                "rsi": result["rsi"],

                "macd": result["macd"],

                "bollinger": result["bollinger"],

                "detail": result["detail"]

            })

        ranking.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        return ranking