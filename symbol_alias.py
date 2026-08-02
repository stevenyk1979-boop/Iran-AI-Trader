"""
Iran AI Trader Professional
Symbol Alias Mapper
"""


class SymbolAlias:


    aliases = {

        "fmelli": "فملی",

        "foolad": "فولاد",

        "khodro": "خودرو",

        "shasta": "شستا",

        "webmelat": "وبملت"

    }


    @classmethod
    def normalize(cls, symbol):

        symbol = str(symbol).strip()

        return cls.aliases.get(
            symbol.lower(),
            symbol
        )