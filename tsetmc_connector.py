"""
Iran AI Trader Professional
TSETMC Connector
"""

import requests

from market_data_adapter import MarketDataAdapter


class TSETMCConnector:


    BASE_URL = "https://cdn.tsetmc.com/api"


    def __init__(self):

        self.connected = False

        self.session = requests.Session()

        self.adapter = MarketDataAdapter()



    def connect(self):

        """
        Initialize TSETMC connection
        """

        self.connected = True


        self.session.headers.update({

            "User-Agent": "Iran-AI-Trader"

        })


        return True



    def status(self):

        return self.connected



    def request(self, endpoint):

        """
        Generic API request
        """

        if not self.connected:

            self.connect()


        url = f"{self.BASE_URL}/{endpoint}"


        response = self.session.get(

            url,

            timeout=10

        )


        response.raise_for_status()


        return response.json()



    def adapt_symbols(self, raw_data):

        """
        Convert raw TSETMC data
        into project format
        """

        return self.adapter.load_symbols(raw_data)



    def get_symbols(self):

        """
        Real symbol list will be connected
        in next Sprint.
        """

        raise NotImplementedError(

            "TSETMC symbol endpoint is not connected yet."

        )