"""
Iran AI Trader Professional
TSETMC Connector
"""

import requests

from symbol_loader import SymbolLoader



class TSETMCConnector:


    BASE_URL = "https://cdn.tsetmc.com/api"


    def __init__(self):

        self.connected = False

        self.session = requests.Session()

        self.symbol_loader = SymbolLoader()



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



    def load_symbols(self, raw_data):

        """
        Process symbol data
        """

        return self.symbol_loader.load_from_tsetmc(raw_data)



    def get_symbols(self):

        """
        Temporary data.
        Real endpoint will replace this.
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


        return self.load_symbols(raw_data)