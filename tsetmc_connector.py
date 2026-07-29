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
        Load symbols into Market Universe
        """

        return self.symbol_loader.load_universe(raw_data)



    def get_market_universe(self):

        """
        Return current Market Universe
        """

        return self.symbol_loader.get_universe()



    def get_symbols(self):

        """
        Temporary symbols.
        Real TSETMC endpoint will replace this.
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


        universe = self.load_symbols(raw_data)


        return universe.symbols()