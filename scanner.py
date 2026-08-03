"""
Iran AI Trader Professional
Scanner Engine Sprint27 Debug
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

from market_service import MarketService
from ranking_service import RankingService

from market_config import MAX_THREADS


class Scanner:

    def __init__(self):

        self.market_service = MarketService()

        self.ranking_service = RankingService()

        self.failed_symbols = []


    # -------------------------------------------------

    def analyze_symbol(self, item):

        symbol = item["symbol"]

        try:

            print(
                f"Scanning {symbol}"
            )


            history = self.market_service.history(

                symbol

            )


            if history is None:

                raise Exception(
                    "No history returned"
                )


            prices = history.close_prices()


            if len(prices) < 20:

                raise Exception(
                    f"Not enough candles: {len(prices)}"
                )


            result = self.ranking_service.analyze(

                history,

                symbol

            )


            return {

                "symbol": symbol,

                "score": result["score"],

                "signal": result["signal"],

                "confidence": result.get(
                    "confidence",
                    0
                ),

                "risk": result.get(
                    "risk",
                    0
                ),

                "price": prices[-1],


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

            }


        except Exception as error:


            print(
                f"FAILED {symbol} -> {error}"
            )


            self.failed_symbols.append({

                "symbol": symbol,

                "error": str(error)

            })


            return None



    # -------------------------------------------------

    def scan(self):


        ranking = []


        symbols = self.market_service.symbols()


        print()

        print(
            f"Total Symbols : {len(symbols)}"
        )


        

        print()

        


        print()

        print(
            "Starting Parallel Scan..."
        )


        with ThreadPoolExecutor(

            max_workers=MAX_THREADS

        ) as executor:


            futures = []


            for item in symbols:

                futures.append(

                    executor.submit(

                        self.analyze_symbol,

                        item

                    )

                )


            completed = 0


            total = len(futures)


            for future in as_completed(futures):


                completed += 1


                result = future.result()


                if result:

                    ranking.append(result)


                print(

                    f"Progress {completed}/{total}"

                )



        ranking.sort(

            key=lambda x: x["score"],

            reverse=True

        )


        print()

        print(
            "=" * 60
        )

        print(
            "Scan Summary"
        )

        print(
            "=" * 60
        )


        print(
            "Successful :",
            len(ranking)
        )


        print(
            "Failed     :",
            len(self.failed_symbols)
        )


        return ranking