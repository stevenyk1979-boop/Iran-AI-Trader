"""
Iran AI Trader Professional
Smart Capital Engine
Sprint32-D
"""

from capital_manager import CapitalManager
from position_sizer import PositionSizer
from portfolio_guard import PortfolioGuard
from risk_manager import RiskManager


class SmartCapitalEngine:

    def __init__(

        self,

        capital=100_000_000,

        risk_percent=1

    ):

        self.capital_manager = CapitalManager(

            capital,

            risk_percent

        )

        self.position_sizer = PositionSizer()

        self.portfolio_guard = PortfolioGuard()

        self.risk_manager = RiskManager()

    # -------------------------------------

    def allocate(

        self,

        candidate,

        market_regime,

        portfolio=None

    ):

        if portfolio is None:

            portfolio = []

        capital_info = self.capital_manager.allocate(

            candidate

        )

        allocation = capital_info[

            "allocation_percent"

        ]

        if market_regime.get(

            "regime"

        ) == "BEAR":

            allocation *= 0.5

            capital_info["capital"] *= 0.5

        allowed = self.portfolio_guard.allow(

            portfolio,

            candidate["symbol"],

            allocation

        )

        if not allowed:

            return {

                "allowed": False,

                "reason": "Portfolio Guard"

            }

        price = candidate.get(

            "price",

            1

        )

        position = self.position_sizer.calculate(

            capital_info["capital"],

            price

        )

        return {

            "allowed": True,

            "allocation_percent": allocation,

            "capital": capital_info["capital"],

            "shares": position["shares"],

            "capital_used": position["capital_used"]

        }