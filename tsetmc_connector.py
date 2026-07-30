"""
Iran AI Trader Professional
TSETMC Connector
"""

import requests


class TSETMCConnector:

    BASE_URL = ""

    def __init__(self):

        self.timeout = 20

    def get(self, url):

        response = requests.get(

            url,

            timeout=self.timeout

        )

        response.raise_for_status()

        return response.text

    def download_symbols(self):

        """
        TODO

        اتصال واقعی TSETMC

        فعلاً None برمی‌گرداند.
        """

        return None

    def download_history(self, symbol):

        """
        TODO

        اتصال واقعی تاریخچه

        """

        return None