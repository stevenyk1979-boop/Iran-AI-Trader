"""
Iran AI Trader V2.0 Alpha
Sample Market
"""

from market_config import USE_REAL_MARKET
from tsetmc_connector import TSETMCConnector


class SampleMarket:

    def __init__(self):

        self.connector = TSETMCConnector()

    def symbols(self):

        if USE_REAL_MARKET:

            self.connector.connect()

            names = self.connector.get_symbols()

            result = []

            for name in names:

                result.append({

                    "symbol": name,

                    "file": f"market_data/{name}.csv"

                })

            return result

        return [

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