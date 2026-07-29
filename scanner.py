"""
Iran AI Trader Professional
Scanner Engine
"""


from market_service import MarketService
from ranking_service import RankingService
from market_universe import MarketUniverse



class Scanner:


    def __init__(self):

        self.market = MarketUniverse()

        self.market_service = MarketService()

        self.ranking_service = RankingService()



    def load_market(self, symbols):

        """
        Load market symbols into universe
        """

        self.market.load(symbols)



    def scan(self):

        """
        Scan all market symbols
        """

        ranking = []


        symbols = self.market.symbols()


        for item in symbols:


            symbol = item["symbol"]

            filename = item["file"]


            try:

                prices = self.market_service.get_prices(filename)


            except FileNotFoundError:

                print(
                    f"Skip {symbol} - data file not found"
                )

                continue


            except Exception as error:

                print(
                    f"Skip {symbol} - {error}"
                )

                continue



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