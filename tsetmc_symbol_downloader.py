"""
Iran AI Trader Professional
TSETMC Symbol Downloader
"""

import csv


class TSETMCSymbolDownloader:

    def __init__(self, connector):

        self.connector = connector

    def download(self):

        """
        دریافت لیست نمادها

        در نسخه فعلی:
        اگر فایل symbols.csv وجود داشته باشد
        آن را می‌خواند.

        در نسخه بعد:
        مستقیماً از TSETMC دانلود خواهد شد.
        """

        rows = []

        try:

            with open(
                "symbols.csv",
                encoding="utf-8-sig"
            ) as file:

                reader = csv.reader(file)

                next(reader, None)

                for row in reader:

                    rows.append(row)

        except FileNotFoundError:

            pass

        return rows