"""
Iran AI Trader Professional
Symbol Manager
"""


class SymbolManager:


    def __init__(self):

        self.symbols = []



    def load(self, symbols):

        """
        Load symbols list
        """

        self.symbols = list(symbols)



    def add(self, symbol):

        """
        Add new symbol
        """

        if symbol not in self.symbols:

            self.symbols.append(symbol)



    def remove(self, symbol):

        """
        Remove symbol
        """

        if symbol in self.symbols:

            self.symbols.remove(symbol)



    def all(self):

        return self.symbols



    def count(self):

        return len(self.symbols)



    def exists(self, symbol):

        return symbol in self.symbols



    def find(self, keyword):

        """
        Search symbols
        """

        result = []

        for symbol in self.symbols:

            if keyword in symbol:

                result.append(symbol)


        return result