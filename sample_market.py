"""
Iran AI Trader V2.0 Alpha
Market Provider
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

                    "file": "historical_data.csv"

                })

            return result

        return [

            {

                "symbol": "وبملت",

                "file": "historical_data.csv"

            },

            {

                "symbol": "فملی",

                "file": "historical_data.csv"

            },

            {

                "symbol": "فولاد",

                "file": "historical_data.csv"

            },

            {

                "symbol": "شستا",

                "file": "historical_data.csv"

            },

            {

                "symbol": "خودرو",

                "file": "historical_data.csv"

            }

        ]