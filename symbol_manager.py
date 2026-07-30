"""
Iran AI Trader Professional
Symbol Manager
"""


from symbol_alias import SymbolAlias



class SymbolManager:


    def __init__(self):

        self.symbols = []



    def normalize(self, symbol):

        """
        Normalize symbol name
        """

        return SymbolAlias.normalize(symbol)



    def load(self, symbols):

        """
        Load symbols list
        with deduplication
        """

        unique = {}


        for item in symbols:


            # Dictionary format

            if isinstance(item, dict):

                raw_symbol = item.get(
                    "symbol"
                )

                if not raw_symbol:

                    continue


                normalized = self.normalize(
                    raw_symbol
                )


                item["symbol"] = normalized


                key = normalized



                # Keep first occurrence

                if key not in unique:

                    unique[key] = item



            # String format

            else:

                raw_symbol = str(item)


                normalized = self.normalize(
                    raw_symbol
                )


                key = normalized



                if key not in unique:

                    unique[key] = normalized



        self.symbols = list(
            unique.values()
        )



    def add(self, symbol):

        """
        Add symbol
        """

        symbol = self.normalize(symbol)


        if symbol not in self.symbols:

            self.symbols.append(symbol)



    def remove(self, symbol):

        """
        Remove symbol
        """

        symbol = self.normalize(symbol)


        if symbol in self.symbols:

            self.symbols.remove(symbol)



    def all(self):

        """
        Return all symbols
        """

        return self.symbols



    def count(self):

        """
        Return symbol count
        """

        return len(self.symbols)



    def exists(self, symbol):

        """
        Check symbol exists
        """

        symbol = self.normalize(symbol)

        return symbol in self.symbols



    def find(self, keyword):

        """
        Search symbols
        """

        keyword = self.normalize(keyword)


        result = []


        for symbol in self.symbols:


            if isinstance(symbol, dict):

                name = symbol.get(
                    "symbol",
                    ""
                )

            else:

                name = symbol



            if keyword in name:

                result.append(symbol)



        return result