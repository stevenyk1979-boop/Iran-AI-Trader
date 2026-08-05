"""
Iran AI Trader Professional

Scanner V2

Sprint44

Market Loader
"""


class MarketLoader:


    def __init__(self):

        self.symbols = []



    def load_symbols(self, data=None):


        if data is None:

            return []



        result = []


        for item in data:


            if item is None:

                continue


            if "symbol" not in item:

                continue


            result.append(item)



        self.symbols = result


        return result



    def count(self):

        return len(
            self.symbols
        )