"""
Iran AI Trader Professional
CSV Loader
"""

import csv
from datetime import datetime, timedelta

from historical_data import HistoricalData
from market_data import MarketData


class CSVLoader:


    def load(self, filename):

        history = HistoricalData()


        symbol = filename.split("/")[-1].replace(".csv", "")
        symbol = symbol.split("\\")[-1]


        with open(
            filename,
            newline="",
            encoding="utf-8-sig"
        ) as file:


            reader = csv.DictReader(file)


            counter = 0


            for row in reader:


                counter += 1


                # Symbol

                candle_symbol = row.get(
                    "symbol",
                    symbol
                )


                # Date handling

                if "date" in row and row["date"]:

                    date = datetime.strptime(
                        row["date"],
                        "%Y-%m-%d"
                    )

                else:

                    date = (
                        datetime.now()
                        -
                        timedelta(
                            days=counter
                        )
                    )


                candle = MarketData(

                    symbol=candle_symbol,

                    date=date,


                    open_price=float(
                        row["open"]
                    ),


                    high_price=float(
                        row["high"]
                    ),


                    low_price=float(
                        row["low"]
                    ),


                    close_price=float(
                        row["close"]
                    ),


                    volume=int(
                        row.get(
                            "volume",
                            0
                        )
                    ),


                    value=float(
                        row.get(
                            "value",
                            0
                        )
                    )

                )


                history.add(candle)


        return history