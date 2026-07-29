"""
Iran AI Trader Professional
Sample Market
"""

from market_config import USE_REAL_MARKET

from tsetmc_connector import TSETMCConnector

from symbol_manager import SymbolManager



class SampleMarket:


    def __init__(self):

        self.connector = TSETMCConnector()

        self.symbol_manager = SymbolManager()



    def symbols(self):

        """
        Return market symbols
        """

        if self.symbol_manager.count() > 0:

            return self.symbol_manager.all()



        if USE_REAL_MARKET:

            self.connector.connect()

            names = self.connector.get_symbols()

            self.symbol_manager.load(names)

            return self.symbol_manager.all()



        sample_symbols = [

            {
                "symbol": "وبملت",
                "file": "market_data/webmelat.csv"
            },

            {
                "symbol": "فملی",
                "file": "market_data/fmelli.csv"
            },

            {
                "symbol": "فولاد",
                "file": "market_data/foolad.csv"
            },

            {
                "symbol": "شستا",
                "file": "market_data/shasta.csv"
            },

            {
                "symbol": "خودرو",
                "file": "market_data/khodro.csv"
            }

        ]


        self.symbol_manager.load(sample_symbols)


        return self.symbol_manager.all()