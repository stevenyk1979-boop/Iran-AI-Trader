"""
Iran AI Trader Professional
Market Data Adapter
"""


class MarketDataAdapter:


    def __init__(self):

        self.symbols = []


    def load_symbols(self, raw_data):

        """
        Convert TSETMC raw response
        to project format
        """

        result = []


        for item in raw_data:

            result.append({

                "symbol": item.get("symbol"),

                "name": item.get("name"),

                "inscode": item.get("inscode"),

                "market": item.get("market"),

                "file": f"market_data/{item.get('symbol')}.csv"

            })


        self.symbols = result


        return result


    def get_symbols(self):

        return self.symbols


    def count(self):

        return len(self.symbols)