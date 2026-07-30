"""
Iran AI Trader Professional
TSETMC Symbol Parser
"""


class TSETMCSymbolParser:

    def parse(self, raw_rows):

        symbols = []

        for row in raw_rows:

            if len(row) < 2:
                continue

            symbol = str(row[0]).strip()

            name = str(row[1]).strip()

            if symbol == "":
                continue

            symbols.append({

                "symbol": symbol,

                "name": name

            })

        return symbols