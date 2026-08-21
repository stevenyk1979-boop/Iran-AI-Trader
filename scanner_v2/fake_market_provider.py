# `scanner_v2/fake/fake_market_provider.py`

"""
Iran AI Trader Professional

Scanner V2

Sprint44-35

Dynamic Fake Market Provider

Purpose:
Provide deterministic but different price histories
for TEST1 ... TEST12 so Ranking Engine can be
validated with genuinely different scores.
"""


class FakeMarketProvider:

    def __init__(self):

        self.symbols = [

            {"symbol": "TEST1"},
            {"symbol": "TEST2"},
            {"symbol": "TEST3"},
            {"symbol": "TEST4"},
            {"symbol": "TEST5"},
            {"symbol": "TEST6"},
            {"symbol": "TEST7"},
            {"symbol": "TEST8"},
            {"symbol": "TEST9"},
            {"symbol": "TEST10"},
            {"symbol": "TEST11"},
            {"symbol": "TEST12"},

        ]

        # Different deterministic market profiles.
        #
        # Higher multiplier = stronger upward trend.
        #
        # TEST1 is intentionally strongest.
        # TEST12 is intentionally weakest.

        self.profiles = {

            "TEST1":  1.30,
            "TEST2":  1.20,
            "TEST3":  1.10,
            "TEST4":  1.00,
            "TEST5":  0.90,
            "TEST6":  0.80,
            "TEST7":  0.70,
            "TEST8":  0.60,
            "TEST9":  0.50,
            "TEST10": 0.40,
            "TEST11": 0.30,
            "TEST12": 0.20,

        }


    def get_symbols(self):

        return self.symbols


    def get_history(self, symbol):

        if symbol not in self.profiles:

            return None

        multiplier = self.profiles[symbol]

        return FakeHistory(
            multiplier=multiplier
        )


class FakeHistory:

    def __init__(
        self,
        multiplier=1.0
    ):

        self.prices = [

            100 + (
                i * multiplier
            )

            for i in range(30)

        ]


    def close_prices(self):

        return self.prices

