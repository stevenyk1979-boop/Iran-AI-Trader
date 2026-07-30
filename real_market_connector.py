"""
Iran AI Trader Professional
Real Market Connector
"""

import requests


class RealMarketConnector:

    def __init__(self):

        self.timeout = 20

        self.connected = False

    # ---------------------------------

    def connect(self):

        self.connected = True

        return True

    # ---------------------------------

    def disconnect(self):

        self.connected = False

    # ---------------------------------

    def status(self):

        return self.connected

    # ---------------------------------

    def request(self, url):

        response = requests.get(

            url,

            timeout=self.timeout

        )

        response.raise_for_status()

        return response.text

    # ---------------------------------

    def download_symbols(self):

        """
        Real Provider

        TODO

        """

        return []

    # ---------------------------------

    def download_history(

        self,

        symbol,

        days=100

    ):

        """
        Real Provider

        TODO

        """

        return []