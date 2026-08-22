"""
Iran AI Trader Professional

Scanner V2

Sprint46

Performance Analytics Engine

Analyzes Trade Journal results and calculates
strategy performance metrics.

IMPORTANT:
No broker connection.
No real order execution.
"""


class PerformanceAnalyticsEngine:

    def __init__(self, trades=None):

        self.trades = []

        if isinstance(trades, list):
            self.trades = list(trades)

    # -------------------------------------------------
    # Set trades
    # -------------------------------------------------

    def set_trades(self, trades):

        if not isinstance(trades, list):

            self.trades = []

            return self.trades

        self.trades = list(trades)

        return self.trades

    # -------------------------------------------------
    # Get trades
    # -------------------------------------------------

    def get_trades(self):

        return list(
            self.trades
        )

    # -------------------------------------------------
    # Safe number
    # -------------------------------------------------

    def _number(
        self,
        value,
        default=0.0
    ):

        try:

            return float(value)

        except Exception:

            return float(default)

    # -------------------------------------------------
    # Winning trades
    # -------------------------------------------------

    def winning_trades(self):

        return [

            trade

            for trade in self.trades

            if isinstance(trade, dict)
            and trade.get(
                "result"
            ) == "WIN"

        ]

    # -------------------------------------------------
    # Losing trades
    # -------------------------------------------------

    def losing_trades(self):

        return [

            trade

            for trade in self.trades

            if isinstance(trade, dict)
            and trade.get(
                "result"
            ) == "LOSS"

        ]

    # -------------------------------------------------
    # Total P/L
    # -------------------------------------------------

    def total_pnl(self):

        return round(
            sum(
                self._number(
                    trade.get(
                        "pnl",
                        0
                    )
                )

                for trade in self.trades

                if isinstance(
                    trade,
                    dict
                )
            ),
            2
        )

    # -------------------------------------------------
    # Total profit
    # -------------------------------------------------

    def total_profit(self):

        return round(
            sum(
                self._number(
                    trade.get(
                        "pnl",
                        0
                    )
                )

                for trade in self.winning_trades()
            ),
            2
        )

    # -------------------------------------------------
    # Total loss
    # -------------------------------------------------

    def total_loss(self):

        return round(
            sum(
                self._number(
                    trade.get(
                        "pnl",
                        0
                    )
                )

                for trade in self.losing_trades()
            ),
            2
        )

    # -------------------------------------------------
    # Win rate
    # -------------------------------------------------

    def win_rate(self):

        total = len(
            self.trades
        )

        if total == 0:
            return 0.0

        wins = len(
            self.winning_trades()
        )

        return round(
            wins /
            total *
            100,
            2
        )

    # -------------------------------------------------
    # Average win
    # -------------------------------------------------

    def average_win(self):

        trades = (
            self.winning_trades()
        )

        if not trades:
            return 0.0

        return round(
            self.total_profit() /
            len(trades),
            2
        )

    # -------------------------------------------------
    # Average loss
    # -------------------------------------------------

    def average_loss(self):

        trades = (
            self.losing_trades()
        )

        if not trades:
            return 0.0

        return round(
            self.total_loss() /
            len(trades),
            2
        )

    # -------------------------------------------------
    # Expectancy
    # -------------------------------------------------

    def expectancy(self):

        total = len(
            self.trades
        )

        if total == 0:
            return 0.0

        win_probability = (
            len(
                self.winning_trades()
            ) /
            total
        )

        loss_probability = (
            len(
                self.losing_trades()
            ) /
            total
        )

        average_win = (
            self.average_win()
        )

        average_loss = abs(
            self.average_loss()
        )

        expectancy = (
            win_probability *
            average_win
            -
            loss_probability *
            average_loss
        )

        return round(
            expectancy,
            2
        )

    # -------------------------------------------------
    # Profit factor
    # -------------------------------------------------

    def profit_factor(self):

        loss = abs(
            self.total_loss()
        )

        if loss == 0:

            if self.total_profit() > 0:
                return float("inf")

            return 0.0

        return round(
            self.total_profit() /
            loss,
            2
        )

    # -------------------------------------------------
    # Equity curve
    # -------------------------------------------------

    def equity_curve(
        self,
        starting_capital=0.0
    ):

        equity = self._number(
            starting_capital
        )

        curve = []

        for index, trade in enumerate(
            self.trades,
            start=1
        ):

            pnl = self._number(
                trade.get(
                    "pnl",
                    0
                )
            )

            equity += pnl

            curve.append({

                "trade":
                    index,

                "symbol":
                    trade.get(
                        "symbol"
                    ),

                "pnl":
                    round(
                        pnl,
                        2
                    ),

                "equity":
                    round(
                        equity,
                        2
                    )

            })

        return curve

    # -------------------------------------------------
    # Maximum drawdown
    # -------------------------------------------------

    def max_drawdown(
        self,
        starting_capital=0.0
    ):

        curve = self.equity_curve(
            starting_capital
        )

        if not curve:
            return 0.0

        peak = self._number(
            starting_capital
        )

        max_drawdown = 0.0

        for item in curve:

            equity = item[
                "equity"
            ]

            if equity > peak:

                peak = equity

            drawdown = (
                peak -
                equity
            )

            if drawdown > max_drawdown:

                max_drawdown = drawdown

        return round(
            max_drawdown,
            2
        )

    # -------------------------------------------------
    # Return percentage
    # -------------------------------------------------

    def return_percent(
        self,
        starting_capital
    ):

        starting_capital = self._number(
            starting_capital
        )

        if starting_capital <= 0:
            return 0.0

        return round(
            self.total_pnl() /
            starting_capital *
            100,
            2
        )

    # -------------------------------------------------
    # Performance status
    # -------------------------------------------------

    def performance_status(self):

        total = len(
            self.trades
        )

        if total == 0:
            return "NO DATA"

        expectancy = (
            self.expectancy()
        )

        profit_factor = (
            self.profit_factor()
        )

        if (
            expectancy > 0
            and profit_factor >= 1.5
        ):

            return "STRONG"

        if (
            expectancy > 0
            and profit_factor >= 1.0
        ):

            return "POSITIVE"

        if expectancy == 0:

            return "NEUTRAL"

        return "WEAK"

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(
        self,
        starting_capital=0.0
    ):

        return {

            "total_trades":
                len(self.trades),

            "wins":
                len(
                    self.winning_trades()
                ),

            "losses":
                len(
                    self.losing_trades()
                ),

            "win_rate_percent":
                self.win_rate(),

            "total_profit":
                self.total_profit(),

            "total_loss":
                self.total_loss(),

            "net_pnl":
                self.total_pnl(),

            "average_win":
                self.average_win(),

            "average_loss":
                self.average_loss(),

            "expectancy":
                self.expectancy(),

            "profit_factor":
                self.profit_factor(),

            "max_drawdown":
                self.max_drawdown(
                    starting_capital
                ),

            "return_percent":
                self.return_percent(
                    starting_capital
                ),

            "performance_status":
                self.performance_status()

        }