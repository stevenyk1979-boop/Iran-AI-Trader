"""
Iran AI Trader Professional
Market Universe
"""


from symbol_manager import SymbolManager



class MarketUniverse:


    def __init__(self):

        self.symbol_manager = SymbolManager()

        self.market = "Iran Stock Market"



    def load(self, symbols):

        """
        Load market symbols
        """

        self.symbol_manager.load(symbols)



    def symbols(self):

        """
        Return all market symbols
        """

        return self.symbol_manager.all()



    def count(self):

        """
        Return symbol count
        """

        return self.symbol_manager.count()



    def exists(self, symbol):

        """
        Check symbol exists
        """

        return self.symbol_manager.exists(symbol)



    def search(self, keyword):

        """
        Search symbols
        """

        return self.symbol_manager.find(keyword)



    def clear(self):

        """
        Clear market universe
        """

        self.symbol_manager.symbols = []



    def status(self):

        """
        Market status
        """

        return {

            "market": self.market,

            "symbols": self.count()

        }