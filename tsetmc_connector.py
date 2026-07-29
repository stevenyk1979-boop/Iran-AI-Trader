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
        Initialize connection
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
        Generic TSETMC request
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
        Convert raw symbols
        """

        return self.adapter.load_symbols(raw_data)



    def get_symbols(self):

        """
        Temporary symbol loader

        Real endpoint will replace this
        """

        raw_data = [

            {
                "symbol": "وبملت",
                "name": "بانک ملت",
                "inscode": "123456",
                "market": "بورس"
            },

            {
                "symbol": "فملی",
                "name": "ملی صنایع مس ایران",
                "inscode": "654321",
                "market": "بورس"
            },

            {
                "symbol": "فولاد",
                "name": "فولاد مبارکه",
                "inscode": "789012",
                "market": "بورس"
            }

        ]


        return self.adapt_symbols(raw_data)