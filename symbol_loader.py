"""
Iran AI Trader Professional
Symbol Loader
"""

from market_universe import MarketUniverse
from tsetmc_symbol_parser import TSETMCSymbolParser
from tsetmc_symbol_downloader import TSETMCSymbolDownloader
from tsetmc_connector import TSETMCConnector


class SymbolLoader:

    def __init__(self):

        self.connector = TSETMCConnector()

        self.downloader = TSETMCSymbolDownloader(
            self.connector
        )

        self.parser = TSETMCSymbolParser()

        self.universe = MarketUniverse()

    def load(self):

        raw_rows = self.downloader.download()

        symbols = self.parser.parse(raw_rows)

        self.universe.load(symbols)

        return self.universe

    def get_symbols(self):

        if self.universe.count() == 0:

            self.load()

        return self.universe.symbols()

    def count(self):

        return self.universe.count()