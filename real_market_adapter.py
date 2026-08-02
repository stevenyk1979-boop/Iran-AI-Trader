"""
Iran AI Trader Professional
Real Market Adapter
"""

from datetime import datetime

import algotik_tse

from historical_data import HistoricalData
from market_data import MarketData


class RealMarketAdapter:

    def __init__(self):

        self.available = True

    # ---------------------------------

    def status(self):

        return self.available

    # ---------------------------------

    def symbols(self):

        df = algotik_tse.get_symbols()

        symbols = []

        for symbol in df.index:

            symbols.append({

                "symbol": symbol

            })

        return symbols

    # ---------------------------------

    def history(

        self,

        symbol,

        days=100

    ):

        df = algotik_tse.get_history(symbol)

        if df is None:

            return None

        history = HistoricalData()

        for index, row in df.iterrows():

            candle = MarketData(

                symbol=symbol,

                
                 date=datetime.now()
                 if "-" in str(index) else datetime.now(),

                open_price=float(row["Open"]),

                high_price=float(row["High"]),

                low_price=float(row["Low"]),

                close_price=float(row["Close"]),

                volume=int(row["Volume"]),

                value=float(row["Close"]) * int(row["Volume"])

            )

            history.add(candle)

        return history