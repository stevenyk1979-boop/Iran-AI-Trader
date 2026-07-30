"""
Iran AI Trader Professional
TSETMC History Provider
"""

from datetime import datetime
from datetime import timedelta


class TSETMCHistory:

    def __init__(self, connector=None):

        self.connector = connector

    def get_history(self, symbol, days=30):
        """
        Get historical candles

        Output:
        [
            [
                date,
                open,
                high,
                low,
                close,
                volume
            ]
        ]
        """

        # TODO:
        # Replace with real TSETMC API

        records = []

        price = 100

        today = datetime.now()

        for i in range(days):

            date = (
                today - timedelta(days=days - i)
            ).strftime("%Y-%m-%d")

            records.append(

                [
                    date,
                    price,
                    price + 2,
                    price - 2,
                    price + 1,
                    1000000,
                ]

            )

            price += 1

        return records

    def download_csv(self, symbol, days=30):
        """
        Return CSV text
        """

        rows = self.get_history(symbol, days)

        csv_text = (
            "date,open,high,low,close,volume\n"
        )

        for row in rows:

            csv_text += (
                f"{row[0]},"
                f"{row[1]},"
                f"{row[2]},"
                f"{row[3]},"
                f"{row[4]},"
                f"{row[5]}\n"
            )

        return csv_text

    def is_available(self):
        """
        Provider status
        """

        return True