"""
Iran AI Trader Professional
TSETMC Connector
"""

import requests


class TSETMCConnector:

    def __init__(self):

        self.timeout = 20

        self.session = requests.Session()

        self.headers = {

            "User-Agent": "Iran-AI-Trader/2.1"

        }

    def get(self, url):

        response = self.session.get(

            url,

            timeout=self.timeout,

            headers=self.headers

        )

        response.raise_for_status()

        return response.text

    def download_symbols(self):

        """
        Download market symbols.

        TODO:
        Replace with real TSETMC endpoint.
        """

        return []

    def download_history(self, symbol):

        """
        Download historical candles.

        TODO:
        Replace with real TSETMC endpoint.
        """

        return []

    def is_available(self):

        """
        Provider status
        """

        return True