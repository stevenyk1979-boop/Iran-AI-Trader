"""
Iran AI Trader Professional

Pipeline Market Data Adapter
Sprint44

Converts Scanner output
to Market Regime V2 input format
"""


class PipelineMarketDataAdapter:


    def __init__(self):

        self.module = "PipelineMarketDataAdapter"



    # -------------------------------------

    def convert(self, ranking):

        """
        Convert pipeline ranking data
        into Market Regime V2 format
        """


        try:


            # اگر Scanner دیکشنری کامل برگرداند

            if isinstance(ranking, dict):

                data = ranking



            # اگر Scanner لیست نمادها را برگرداند

            elif isinstance(ranking, list):


                total = len(ranking)


                positive = 0

                negative = 0

                unchanged = 0


                scores = []



                for item in ranking:


                    if isinstance(item, dict):


                        score = item.get(

                            "score",

                            50

                        )


                        scores.append(score)



                        if score >= 70:

                            positive += 1


                        elif score <= 40:

                            negative += 1


                        else:

                            unchanged += 1



                avg_score = (

                    sum(scores) / len(scores)

                    if scores

                    else 50

                )



                data = {


                    "price": avg_score,


                    "ema20": avg_score,


                    "ema50": avg_score - 2,


                    "ema100": avg_score - 5,


                    "ema50_prev": avg_score - 3,


                    "positive": positive,


                    "negative": negative,


                    "unchanged": unchanged,


                    "volume": 1,


                    "avg_volume": 1,


                    "value": 1,


                    "avg_value": 1,


                    "money_flow": avg_score,


                    "atr_percent": 2,


                    "market_volatility": 2,


                    "drawdown": 5,


                    "index_change": 0,


                    "equal_change": 0

                }



            else:


                raise Exception(

                    "Unsupported ranking format"

                )



            return data



        except Exception as e:



            return {


                "price": 50,

                "ema20": 50,

                "ema50": 50,

                "ema100": 50,

                "ema50_prev": 50,

                "positive": 0,

                "negative": 0,

                "unchanged": 0,

                "volume": 1,

                "avg_volume": 1,

                "value": 1,

                "avg_value": 1,

                "money_flow": 50,

                "atr_percent": 2,

                "market_volatility": 2,

                "drawdown": 0,

                "index_change": 0,

                "equal_change": 0

            }



    # -------------------------------------

    def status(self):


        return {


            "module": self.module,


            "active": True

        }