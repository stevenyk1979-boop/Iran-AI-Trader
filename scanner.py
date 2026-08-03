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

    # ------------------------------------------------------------

    def scan(self):

        ranking = []

        symbols = self.market_service.symbols()

        print(f"Total Symbols : {len(symbols)}")

        # برای تست در صورت نیاز
        # symbols = symbols[:10]

        for index, item in enumerate(symbols, start=1):

            symbol = item["symbol"]

            print(f"[{index}/{len(symbols)}] {symbol}")

            # ----------------------------------------------------

            try:

                history = self.market_service.history(symbol)

            except Exception as error:

                print(f"Skip {symbol} - {error}")
                continue

            if history is None:

                continue

            # ----------------------------------------------------

            try:

                prices = history.close_prices()

            except Exception:

                continue

            if len(prices) < 20:

                continue

            # ----------------------------------------------------

            try:

                decision = self.ranking_service.analyze(

                    history,

                    symbol

                )

            except Exception as error:

                print(f"AI Error {symbol} - {error}")
                continue

            # ----------------------------------------------------

            ranking.append({

                "decision": decision,

                "symbol": decision.symbol,

                "score": round(decision.score, 2),

                "signal": decision.signal,

                "confidence": round(decision.confidence, 2),

                "risk": round(decision.risk, 2),

                "price": prices[-1],

                "reasons": decision.reasons,

                "detail": decision.detail

            })

        # ----------------------------------------------------

        ranking.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        return ranking