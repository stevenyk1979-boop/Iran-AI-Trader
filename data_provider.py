"""
Iran AI Trader V2.0 Alpha
Data Provider
"""

from market_config import DATA_SOURCE
from market_config import DEFAULT_HISTORY_FILE

from csv_loader import CSVLoader


class DataProvider:

    def __init__(self):

        self.loader = CSVLoader()

    def load_history(self, filename=None):

        if filename is None:

            filename = DEFAULT_HISTORY_FILE

        if DATA_SOURCE == "CSV":

            return self.loader.load(filename)

        raise NotImplementedError(
            f"{DATA_SOURCE} provider not implemented."
        )

    def get_prices(self, filename=None):

        history = self.load_history(filename)

        return history.close_prices()

    def get_last_record(self, filename=None):

        history = self.load_history(filename)

        return history.last()

    def get_symbol(self, filename=None):

        last = self.get_last_record(filename)

        if last:

            return last.symbol

        return None