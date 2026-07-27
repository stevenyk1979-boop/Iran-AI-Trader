"""
Iran AI Trader V2.0
Historical Data Engine
"""

from datetime import datetime

from market_data import MarketData


class HistoricalData:

    def __init__(self):

        self.candles = []

    def add(self, candle: MarketData):

        self.candles.append(candle)

    def count(self):

        return len(self.candles)

    def close_prices(self):

        return [
            candle.close_price
            for candle in self.candles
        ]

    def last(self):

        if not self.candles:
            return None

        return self.candles[-1]

    def load_sample_data(self):

        prices = [

            100,
            101,
            102,
            103,
            104,
            106,
            108,
            107,
            110,
            112,
            113,
            115,
            117,
            118,
            120,
            122,
            121,
            123,
            124,
            126

        ]

        for p in prices:

            candle = MarketData(

                symbol="وبملت",

                date=datetime.now(),

                open_price=p,

                high_price=p + 2,

                low_price=p - 2,

                close_price=p,

                volume=100000,

                value=p * 100000

            )

            self.add(candle)