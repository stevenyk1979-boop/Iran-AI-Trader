"""
Iran AI Trader Professional

Scanner V2

Sprint47

Recovery Analytics Engine

Tracks:
- Peak equity
- Drawdown bottom
- Recovery amount
- Recovery percentage
- Recovery status
- Recovery duration

IMPORTANT:
No broker connection.
No real order execution.
"""


class RecoveryAnalyticsEngine:

    def __init__(
        self,
        starting_capital=0.0
    ):

        self.starting_capital = float(
            starting_capital
        )

        self.equity = (
            self.starting_capital
        )

        self.peak_equity = (
            self.starting_capital
        )

        self.drawdown_bottom = (
            self.starting_capital
        )

        self.max_drawdown = 0.0

        self.max_drawdown_percent = 0.0

        self.recovery_amount = 0.0

        self.recovery_percent = 0.0

        self.recovery_duration = 0

        self.max_recovery_duration = 0

        self.history = []

    # -------------------------------------------------
    # Reset
    # -------------------------------------------------

    def reset(
        self,
        starting_capital=None
    ):

        if starting_capital is not None:

            self.starting_capital = float(
                starting_capital
            )

        self.equity = (
            self.starting_capital
        )

        self.peak_equity = (
            self.starting_capital
        )

        self.drawdown_bottom = (
            self.starting_capital
        )

        self.max_drawdown = 0.0

        self.max_drawdown_percent = 0.0

        self.recovery_amount = 0.0

        self.recovery_percent = 0.0

        self.recovery_duration = 0

        self.max_recovery_duration = 0

        self.history = []

        return self.current_state()

    # -------------------------------------------------
    # Update equity
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

        previous_equity = (
            self.equity
        )

        self.equity += pnl

        # -------------------------------------------------
        # New peak
        # -------------------------------------------------

        if self.equity >= self.peak_equity:

            # If we were recovering and reach
            # the previous peak, recovery is complete.

            if (
                self.recovery_duration > 0
                and
                self.equity >= self.peak_equity
            ):

                self.max_recovery_duration = max(

                    self.max_recovery_duration,

                    self.recovery_duration

                )

            self.peak_equity = (
                self.equity
            )

            self.drawdown_bottom = (
                self.equity
            )

            self.recovery_amount = 0.0

            self.recovery_percent = 100.0

            self.recovery_duration = 0

        else:

            # -------------------------------------------------
            # Drawdown
            # -------------------------------------------------

            drawdown = (
                self.peak_equity -
                self.equity
            )

            if self.equity < self.drawdown_bottom:

                self.drawdown_bottom = (
                    self.equity
                )

            self.max_drawdown = max(

                self.max_drawdown,

                drawdown

            )

            if self.peak_equity > 0:

                dd_percent = (
                    drawdown /
                    self.peak_equity *
                    100
                )

            else:

                dd_percent = 0.0

            self.max_drawdown_percent = max(

                self.max_drawdown_percent,

                dd_percent

            )

            # -------------------------------------------------
            # Recovery
            # -------------------------------------------------

            total_recovery_needed = (
                self.peak_equity -
                self.drawdown_bottom
            )

            self.recovery_amount = (
                self.equity -
                self.drawdown_bottom
            )

            if total_recovery_needed > 0:

                self.recovery_percent = (

                    self.recovery_amount /
                    total_recovery_needed
                ) * 100

            else:

                self.recovery_percent = 0.0

            # Count periods spent below peak.

            if previous_equity < self.peak_equity:

                self.recovery_duration += 1

        state = self.current_state()

        self.history.append(
            state
        )

        return state

    # -------------------------------------------------
    # Process P/L sequence
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

            self.update(
                trade.get(
                    "pnl",
                    0
                )
            )

        return list(
            self.history
        )

    # -------------------------------------------------
    # Recovery status
    # -------------------------------------------------

    def recovery_status(self):

        if self.equity >= self.peak_equity:

            return "FULLY RECOVERED"

        if self.recovery_percent >= 75:

            return "NEAR RECOVERY"

        if self.recovery_percent > 0:

            return "RECOVERING"

        return "DRAWDOWN"

    # -------------------------------------------------
    # Current state
    # -------------------------------------------------

    def current_state(self):

        return {

            "equity":
                round(
                    self.equity,
                    2
                ),

            "peak_equity":
                round(
                    self.peak_equity,
                    2
                ),

            "drawdown_bottom":
                round(
                    self.drawdown_bottom,
                    2
                ),

            "max_drawdown":
                round(
                    self.max_drawdown,
                    2
                ),

            "max_drawdown_percent":
                round(
                    self.max_drawdown_percent,
                    2
                ),

            "recovery_amount":
                round(
                    self.recovery_amount,
                    2
                ),

            "recovery_percent":
                round(
                    self.recovery_percent,
                    2
                ),

            "recovery_duration":
                self.recovery_duration,

            "max_recovery_duration":
                self.max_recovery_duration,

            "recovery_status":
                self.recovery_status()

        }