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


    # ---------------------------------

    def scan(self):

        ranking = []

        symbols = self.market_service.symbols()


        # تست محدود (فعلاً برای Integration Test)
        # بعد از موفقیت حذف می‌کنیم
        # symbols = symbols[:10]


        for item in symbols:

            symbol = item["symbol"]


            try:

                history = self.market_service.history(

                    symbol

                )


            except Exception as error:

                print(

                    f"Skip {symbol} - {error}"

                )

                continue



            if history is None:

                continue



            try:

                prices = history.close_prices()


            except Exception:

                continue



            if len(prices) < 20:

                continue



            try:

                result = self.ranking_service.analyze(

                    history,

                    symbol

                )


            except Exception as error:

                print(

                    f"AI Error {symbol} - {error}"

                )

                continue



            ranking.append({

                "symbol": symbol,

                "score": result["score"],

                "signal": result["signal"],

                "price": prices[-1],


                # AI Information

                "confidence": result.get(

                    "confidence",

                    0

                ),

                "risk": result.get(

                    "risk",

                    0

                ),


                # Technical Data

                "rsi": result.get(

                    "rsi"

                ),

                "macd": result.get(

                    "macd"

                ),

                "bollinger": result.get(

                    "bollinger"

                ),


                "detail": result.get(

                    "detail"

                )

            })



        ranking.sort(

            key=lambda x: x["score"],

            reverse=True

        )


        return ranking