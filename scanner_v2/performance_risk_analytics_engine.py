"""
Iran AI Trader Professional

Scanner V2

Sprint51

Performance + Risk + Strategy Quality Integration Engine

Combines:

Trade Journal
        ↓
Performance Analytics
        ↓
Equity Curve
        ↓
Drawdown Analytics
        ↓
Recovery Analytics
        ↓
Strategy Quality Score

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

from scanner_v2.strategy_quality_score_engine import (
    StrategyQualityScoreEngine
)

from scanner_v2.recovery_analytics_adapter import (
    RecoveryAnalyticsAdapter
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

        self.quality_engine = (
            StrategyQualityScoreEngine()
        )

        self.recovery_adapter = (
            RecoveryAnalyticsAdapter()
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
    # Recovery statistics
    # -------------------------------------------------

    def recovery_statistics(self):

        equity = (
            self.equity_statistics()
        )

        return self.recovery_adapter.calculate(
            equity
        )

    # -------------------------------------------------
    # Strategy quality
    # -------------------------------------------------

    def strategy_quality(self):

        performance = (
            self.performance_statistics()
        )

        equity = (
            self.equity_statistics()
        )

        recovery = (
            self.recovery_statistics()
        )

        performance_data = {

            "return_percent":
                performance.get(
                    "return_percent",
                    0.0
                ),

            "win_rate_percent":
                performance.get(
                    "win_rate_percent",
                    0.0
                ),

            "profit_factor":
                performance.get(
                    "profit_factor",
                    0.0
                ),

            "max_drawdown_percent":
                equity.get(
                    "max_drawdown_percent",
                    0.0
                ),

            "recovery_percent":
                recovery.get(
                    "recovery_percent",
                    0.0
                )

        }

        return self.quality_engine.evaluate(
            performance_data
        )

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

        recovery = (
            self.recovery_statistics()
        )

        quality = (
            self.strategy_quality()
        )

        return {

            "total_trades":
                performance.get(
                    "total_trades",
                    0
                ),

            "wins":
                performance.get(
                    "wins",
                    0
                ),

            "losses":
                performance.get(
                    "losses",
                    0
                ),

            "win_rate_percent":
                performance.get(
                    "win_rate_percent",
                    0.0
                ),

            "net_pnl":
                performance.get(
                    "net_pnl",
                    0.0
                ),

            "expectancy":
                performance.get(
                    "expectancy",
                    0.0
                ),

            "profit_factor":
                performance.get(
                    "profit_factor",
                    0.0
                ),

            "equity":
                equity.get(
                    "equity",
                    self.starting_capital
                ),

            "peak_equity":
                equity.get(
                    "peak_equity",
                    self.starting_capital
                ),

            "drawdown":
                equity.get(
                    "drawdown",
                    0.0
                ),

            "drawdown_percent":
                equity.get(
                    "drawdown_percent",
                    0.0
                ),

            "max_drawdown":
                equity.get(
                    "max_drawdown",
                    0.0
                ),

            "max_drawdown_percent":
                equity.get(
                    "max_drawdown_percent",
                    0.0
                ),

            "recovery_percent":
                recovery.get(
                    "recovery_percent",
                    0.0
                ),

            "recovery_status":
                recovery.get(
                    "recovery_status",
                    "DRAWDOWN"
                ),

            "return_percent":
                performance.get(
                    "return_percent",
                    0.0
                ),

            "performance_status":
                performance.get(
                    "performance_status",
                    "UNKNOWN"
                ),

            "strategy_quality_score":
                quality.get(
                    "score",
                    0.0
                ),

            "strategy_quality_status":
                quality.get(
                    "status",
                    "DANGEROUS"
                )

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