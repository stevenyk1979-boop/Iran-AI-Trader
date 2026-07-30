"""
Iran AI Trader Professional
TSETMC Connector
"""


import requests



class TSETMCConnector:


    def __init__(self):

        self.connected = False

        self.base_url = "https://www.tsetmc.com"



    def connect(self):

        """
        Initialize connection
        """

        self.connected = True

        return True



    def status(self):

        return self.connected



    def get_symbols(self):

        """
        Return market symbols.

        Compatible with:
        SymbolLoader
        MarketUniverse
        Scanner
        """


        if not self.connected:

            self.connect()



        symbols = [

            "وبملت",

            "فملی",

            "فولاد",

            "شستا",

            "خودرو"

        ]



        result = []



        for symbol in symbols:


            result.append({

                "symbol": symbol,

                "file": f"market_data/{symbol}.csv"

            })



        return result



    def get_symbol_info(self, symbol):

        """
        Symbol information
        """


        return {

            "symbol": symbol,

            "market": "TSE",

            "status": "active"

        }



    def request(self, endpoint):

        """
        Generic HTTP request handler.

        Used later for real TSETMC API.
        """


        if not self.connected:

            self.connect()



        try:

            response = requests.get(

                self.base_url + endpoint,

                timeout=10

            )


            return response.text



        except Exception:


            return None