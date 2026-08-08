"""
Iran AI Trader Professional

Scanner V2

Sprint44-11

Fake Market Provider
"""


class FakeMarketProvider:


    def __init__(self):

        self.symbols = [

            {
                "symbol": "TEST1"
            },

            {
                "symbol": "TEST2"
            }

        ]


    def get_symbols(self):

        return self.symbols


    def get_history(self, symbol):

        if symbol not in [
            item["symbol"]
            for item in self.symbols
        ]:

            return None

        return FakeHistory()


class FakeHistory:


    def __init__(self):

        self.prices = [

            100,
            101,
            102,
            103,
            104,
            105,
            106,
            107,
            108,
            109,
            110,
            111,
            112,
            113,
            114,
            115,
            116,
            117,
            118,
            119
        ]


    def close_prices(self):

        return self.prices