"""
Iran AI Trader Professional
Provider Factory
"""

from market_config import DATA_SOURCE

from csv_provider import CSVProvider
from tsetmc_provider import TSETMCProvider


class ProviderFactory:

    @staticmethod
    def create():

        if DATA_SOURCE.upper() == "CSV":
            return CSVProvider()

        if DATA_SOURCE.upper() == "TSETMC":
            return TSETMCProvider()

        raise ValueError(
            f"Unknown data source: {DATA_SOURCE}"
        )