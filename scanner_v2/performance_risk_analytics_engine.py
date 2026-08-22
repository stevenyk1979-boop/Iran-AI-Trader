"""
Iran AI Trader Professional

Scanner V2

Sprint46

Performance + Equity/Drawdown Integration Engine

Combines:

Trade Journal
        ↓
Performance Analytics
        ↓
Equity Curve
        ↓
Drawdown Analytics

IMPORTANT:
No broker connection.
No real order execution.
"""


from scanner_v2.performance_analytics_engine import (
    PerformanceAnalyticsEngine
)

from scanner_v2.equity_drawdown_engine import (
    EquityDrawdownEngine
)


class PerformanceRiskAnalyticsEngine:

    def __init__(
        self,
        trades=None,
        starting_capital=0.0
    ):

        self.trades = (
            trades
            if isinstance(trades, list)
            else []
        )

        self.starting_capital = float(
            starting_capital
        )

        self.performance_engine = (
            PerformanceAnalyticsEngine(
                self.trades
            )
        )

        self.equity_engine = (
            EquityDrawdownEngine(
                self.starting_capital
            )
        )

    # -------------------------------------------------
    # Refresh
    # -------------------------------------------------

    def refresh(
        self,
        trades=None
    ):

        if trades is not None:

            self.trades = (
                trades
                if isinstance(trades, list)
                else []
            )

            self.performance_engine = (
                PerformanceAnalyticsEngine(
                    self.trades
                )
            )

        self.equity_engine.process_trades(
            self.trades
        )

        return self.summary()

    # -------------------------------------------------
    # Performance statistics
    # -------------------------------------------------

    def performance_statistics(self):

        return self.performance_engine.statistics(
            self.starting_capital
        )

    # -------------------------------------------------
    # Equity statistics
    # -------------------------------------------------

    def equity_statistics(self):

        return self.equity_engine.current_state()

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    def summary(self):

        performance = (
            self.performance_statistics()
        )

        equity = (
            self.equity_statistics()
        )

        return {

            "total_trades":
                performance[
                    "total_trades"
                ],

            "wins":
                performance[
                    "wins"
                ],

            "losses":
                performance[
                    "losses"
                ],

            "win_rate_percent":
                performance[
                    "win_rate_percent"
                ],

            "net_pnl":
                performance[
                    "net_pnl"
                ],

            "expectancy":
                performance[
                    "expectancy"
                ],

            "profit_factor":
                performance[
                    "profit_factor"
                ],

            "equity":
                equity[
                    "equity"
                ],

            "peak_equity":
                equity[
                    "peak_equity"
                ],

            "drawdown":
                equity[
                    "drawdown"
                ],

            "drawdown_percent":
                equity[
                    "drawdown_percent"
                ],

            "max_drawdown":
                equity[
                    "max_drawdown"
                ],

            "max_drawdown_percent":
                equity[
                    "max_drawdown_percent"
                ],

            "return_percent":
                performance[
                    "return_percent"
                ],

            "performance_status":
                performance[
                    "performance_status"
                ]

        }

    # -------------------------------------------------
    # Equity curve
    # -------------------------------------------------

    def equity_curve(self):

        return (
            self.equity_engine.equity_curve()
        )

    # -------------------------------------------------
    # Maximum drawdown
    # -------------------------------------------------

    def max_drawdown(self):

        return (
            self.equity_engine.max_drawdown()
        )

    # -------------------------------------------------
    # Maximum drawdown %
    # -------------------------------------------------

    def max_drawdown_percent(self):

        return (
            self.equity_engine.max_drawdown_percent()
        )