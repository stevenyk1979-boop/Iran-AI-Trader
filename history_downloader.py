"""
Iran AI Trader Professional
Historical Data Downloader
"""

from pathlib import Path
import csv
import time


class HistoryDownloader:


    def __init__(self):

        self.data_dir = Path("market_data")

        self.data_dir.mkdir(
            exist_ok=True
        )



    def file_path(self, symbol):

        """
        Return CSV path for symbol
        """

        return self.data_dir / f"{symbol}.csv"



    def exists(self, symbol):

        """
        Check cached history
        """

        return self.file_path(symbol).exists()



    def save(self, symbol, records):

        """
        Save historical records
        """

        path = self.file_path(symbol)


        with open(
            path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:


            writer = csv.writer(file)


            writer.writerow([

                "date",
                "open",
                "high",
                "low",
                "close",
                "volume"

            ])


            for row in records:

                writer.writerow(row)



        return path



    def download(self, symbol):

        """
        Temporary downloader.

        Real TSETMC history endpoint
        will replace this section.
        """


        if self.exists(symbol):

            return self.file_path(symbol)



        sample = []


        price = 100


        for i in range(30):

            sample.append([

                f"2026-07-{i+1}",

                price,

                price + 2,

                price - 2,

                price + 1,

                1000000

            ])


            price += 1



        path = self.save(

            symbol,

            sample

        )


        time.sleep(0.1)


        return path