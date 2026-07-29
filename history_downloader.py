"""
Iran AI Trader Professional
Historical Data Downloader
"""

from pathlib import Path

from tsetmc_history import TSETMCHistory



class HistoryDownloader:


    def __init__(self):

        self.data_dir = Path("market_data")

        self.data_dir.mkdir(
            exist_ok=True
        )

        self.provider = TSETMCHistory()



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
        Save historical candles
        """

        path = self.file_path(symbol)


        with open(
            path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:


            import csv


            writer = csv.writer(file)


            writer.writerow([

                "date",
                "open",
                "high",
                "low",
                "close",
                "volume"

            ])


            writer.writerows(records)



        return path



    def download(self, symbol):

        """
        Download and cache history
        """


        if self.exists(symbol):

            return self.file_path(symbol)



        records = self.provider.get_history(

            symbol

        )


        return self.save(

            symbol,

            records

        )