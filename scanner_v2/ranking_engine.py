"""
Iran AI Trader Professional

Scanner V2

Sprint44-08

Ranking Engine Config Connected
"""


from scanner_v2.config import ScannerConfig



class RankingEngine:


    def __init__(self):

        self.config = ScannerConfig()

        self.results = []



    def analyze(
        self,
        history,
        symbol
    ):


        try:


            if history is None:

                raise Exception(
                    "No history"
                )


            prices = history.close_prices()


            if prices is None:

                raise Exception(
                    "No prices"
                )


            if len(prices) < self.config.get_minimum_candles():

                raise Exception(
                    "Not enough candles"
                )



            score = self.calculate_score(

                prices

            )



            result = {

                "symbol": symbol,

                "score": score,

                "decision": self.decision(score)

            }



            self.results.append(

                result

            )



            return result



        except Exception as error:


            return {

                "symbol": symbol,

                "score": 0,

                "decision": "FAILED",

                "error": str(error)

            }




    def calculate_score(
        self,
        prices
    ):


        start = prices[0]

        end = prices[-1]



        if start <= 0:

            return 0



        change = (

            (end - start)

            /

            start

        ) * 100



        score = 50 + change



        if score > 100:

            score = 100



        if score < 0:

            score = 0



        return round(

            score,

            2

        )




    def decision(
        self,
        score
    ):


        minimum_score = self.config.get_minimum_score()



        if score >= 80:

            return "STRONG WATCH"



        if score >= minimum_score:

            return "WATCH"



        return "IGNORE"