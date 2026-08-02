"""
Iran AI Trader Professional
Provider Factory
"""

from market_config import DATA_SOURCE

from csv_provider import CSVProvider
from tsetmc_provider import TSETMCProvider
from real_market_provider import RealMarketProvider


class ProviderFactory:

    @staticmethod
    def create():

        source = DATA_SOURCE.upper()

        if source == "CSV":
            return CSVProvider()

        if source == "TSETMC":
            return TSETMCProvider()

        if source == "REAL":
            return RealMarketProvider()

        raise ValueError(
            f"Unknown data source: {DATA_SOURCE}"
        )