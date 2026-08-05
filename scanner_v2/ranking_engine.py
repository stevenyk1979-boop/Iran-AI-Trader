"""
Iran AI Trader Professional

Scanner V2

Sprint44-04

Ranking Engine
"""


class RankingEngine:


    def __init__(self):

        self.results = []



    def analyze(self, history, symbol):


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


            if len(prices) < 20:

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


            self.results.append(result)


            return result



        except Exception as error:


            return {

                "symbol": symbol,

                "score": 0,

                "decision": "FAILED",

                "error": str(error)

            }



    def calculate_score(self, prices):


        start = prices[0]

        end = prices[-1]


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



    def decision(self, score):


        if score >= 80:

            return "STRONG WATCH"



        if score >= 60:

            return "WATCH"



        return "IGNORE"