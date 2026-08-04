"""
Iran AI Trader Professional
Portfolio Guard
Sprint32-C
"""


class PortfolioGuard:

    def __init__(

        self,

        max_positions=5,

        max_symbol_percent=20

    ):

        self.max_positions = max_positions

        self.max_symbol_percent = max_symbol_percent

    # --------------------------------------

    def allow(

        self,

        portfolio,

        symbol,

        allocation_percent

    ):

        if len(portfolio) >= self.max_positions:

            return False

        if allocation_percent > self.max_symbol_percent:

            return False

        return True