"""
Iran AI Trader Professional

Scanner V2

Sprint46

Equity Curve + Drawdown Engine

Tracks:
- Equity curve
- Peak equity
- Current drawdown
- Maximum drawdown
- Drawdown percentage

IMPORTANT:
No broker connection.
No real order execution.
"""


class EquityDrawdownEngine:

    def __init__(
        self,
        starting_capital=0.0
    ):

        try:

            self.starting_capital = float(
                starting_capital
            )

        except Exception:

            self.starting_capital = 0.0

        self.equity = (
            self.starting_capital
        )

        self.peak_equity = (
            self.starting_capital
        )

        self.max_drawdown_value = 0.0

        # FIX:
        # Do not use the same name as the
        # max_drawdown_percent() method.

        self.max_drawdown_percent_value = 0.0

        self.history = []

    # -------------------------------------------------
    # Reset
    # -------------------------------------------------

    def reset(
        self,
        starting_capital=None
    ):

        if starting_capital is not None:

            try:

                self.starting_capital = float(
                    starting_capital
                )

            except Exception:

                self.starting_capital = 0.0

        self.equity = (
            self.starting_capital
        )

        self.peak_equity = (
            self.starting_capital
        )

        self.max_drawdown_value = 0.0

        self.max_drawdown_percent_value = 0.0

        self.history = []

        return self.current_state()

    # -------------------------------------------------
    # Apply P/L
    # -------------------------------------------------

    def update(
        self,
        pnl
    ):

        try:

            pnl = float(
                pnl
            )

        except Exception:

            pnl = 0.0

        self.equity += pnl

        # -------------------------------------------------
        # Peak equity
        # -------------------------------------------------

        if self.equity > self.peak_equity:

            self.peak_equity = (
                self.equity
            )

        # -------------------------------------------------
        # Current drawdown
        # -------------------------------------------------

        drawdown = (
            self.peak_equity -
            self.equity
        )

        # -------------------------------------------------
        # Maximum drawdown value
        # -------------------------------------------------

        if drawdown > self.max_drawdown_value:

            self.max_drawdown_value = (
                drawdown
            )

        # -------------------------------------------------
        # Current drawdown percentage
        # -------------------------------------------------

        if self.peak_equity > 0:

            drawdown_percent = (
                drawdown /
                self.peak_equity *
                100
            )

        else:

            drawdown_percent = 0.0

        # -------------------------------------------------
        # Maximum drawdown percentage
        # -------------------------------------------------

        if (
            drawdown_percent >
            self.max_drawdown_percent_value
        ):

            self.max_drawdown_percent_value = (
                drawdown_percent
            )

        # -------------------------------------------------
        # History
        # -------------------------------------------------

        self.history.append({

            "pnl": round(
                pnl,
                2
            ),

            "equity": round(
                self.equity,
                2
            ),

            "peak_equity": round(
                self.peak_equity,
                2
            ),

            "drawdown": round(
                drawdown,
                2
            ),

            "drawdown_percent": round(
                drawdown_percent,
                2
            )

        })

        return self.current_state()

    # -------------------------------------------------
    # Process trades
    # -------------------------------------------------

    def process_trades(
        self,
        trades
    ):

        self.reset()

        if not isinstance(
            trades,
            list
        ):

            return self.history

        for trade in trades:

            if not isinstance(
                trade,
                dict
            ):

                continue

            pnl = trade.get(
                "pnl",
                0
            )

            self.update(
                pnl
            )

        return list(
            self.history
        )

    # -------------------------------------------------
    # Current equity
    # -------------------------------------------------

    def current_equity(self):

        return round(
            self.equity,
            2
        )

    # -------------------------------------------------
    # Peak equity
    # -------------------------------------------------

    def current_peak(self):

        return round(
            self.peak_equity,
            2
        )

    # -------------------------------------------------
    # Current drawdown
    # -------------------------------------------------

    def current_drawdown(self):

        return round(
            self.peak_equity -
            self.equity,
            2
        )

    # -------------------------------------------------
    # Current drawdown percent
    # -------------------------------------------------

    def current_drawdown_percent(self):

        if self.peak_equity <= 0:

            return 0.0

        return round(

            (
                self.current_drawdown()
                /
                self.peak_equity
            ) * 100,

            2

        )

    # -------------------------------------------------
    # Maximum drawdown
    # -------------------------------------------------

    def max_drawdown(self):

        return round(
            self.max_drawdown_value,
            2
        )

    # -------------------------------------------------
    # Maximum drawdown percent
    # -------------------------------------------------

    def max_drawdown_percent(self):

        return round(
            self.max_drawdown_percent_value,
            2
        )

    # -------------------------------------------------
    # Equity curve
    # -------------------------------------------------

    def equity_curve(self):

        return list(
            self.history
        )

    # -------------------------------------------------
    # Current state
    # -------------------------------------------------

    def current_state(self):

        return {

            "equity":
                self.current_equity(),

            "peak_equity":
                self.current_peak(),

            "drawdown":
                self.current_drawdown(),

            "drawdown_percent":
                self.current_drawdown_percent(),

            "max_drawdown":
                self.max_drawdown(),

            "max_drawdown_percent":
                self.max_drawdown_percent(),

            "trades":
                len(self.history)

        }