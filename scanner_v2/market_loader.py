"""
Iran AI Trader Professional

Scanner V2

Sprint44-06

Market Loader
"""


class MarketLoader:


    def __init__(self):

        self.symbols = [

            {
                "symbol": "TEST1"
            },

            {
                "symbol": "TEST2"
            }

        ]



    def load_symbols(self, data=None):


        if data is None:

            data = self.symbols



        result = []



        for item in data:


            if item is None:

                continue



            if "symbol" not in item:

                continue



            result.append(

                item["symbol"]

            )



        self.symbols = result


        return result



    def count(self):

        return len(

            self.symbols

        )