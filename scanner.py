"""
Iran AI Trader Professional
Scanner Engine
Sprint28-A
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

from market_service import MarketService
from ranking_service import RankingService
from watchlist import WatchList

from market_config import MAX_THREADS


class Scanner:

    def __init__(self):

        self.market_service = MarketService()

        self.ranking_service = RankingService()

        self.watchlist = WatchList()

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
                    "Not enough candles"
                )


            result = self.ranking_service.analyze(

                history,

                symbol

            )


            return result



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

    def update_watchlist(

        self,

        ranking

    ):

        """
        Add strong opportunities
        to AI Watch List
        """


        for item in ranking:


            if item["score"] >= 70:


                symbol = item["symbol"]


                if not self.watchlist.exists(

                    symbol

                ):


                    self.watchlist.add(

                        symbol,

                        item["score"],

                        item["signal"],

                        item.get(

                            "detail",

                            {}

                        )

                    )


    # -------------------------------------------------

    def scan(self):


        ranking = []


        symbols = self.market_service.symbols()


        print()

        print(

            f"Total Symbols : {len(symbols)}"

        )


        print()

        print(

            f"Symbols To Scan : {len(symbols)}"

        )


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


                    ranking.append({

                        "symbol": result["symbol"],

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

                        "price": result.get(

                            "price"

                        ),

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



                if completed % 50 == 0:


                    print(

                        f"Processed {completed}/{total}"

                    )



        ranking.sort(

            key=lambda x: x["score"],

            reverse=True

        )



        # Update AI Watch List

        self.update_watchlist(

            ranking

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