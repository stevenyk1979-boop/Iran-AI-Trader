"""
Iran AI Trader Professional

Scanner V2

Sprint51

Recovery Analytics Adapter

Connects the existing Recovery Analytics Engine
to the Performance Risk Analytics pipeline.

IMPORTANT:
No broker connection.
No real order execution.
"""


class RecoveryAnalyticsAdapter:

    def __init__(
        self,
        recovery_engine=None
    ):

        self.recovery_engine = (
            recovery_engine
        )

    def _safe_value(
        self,
        data,
        key,
        default=0.0
    ):

        try:

            return float(
                data.get(
                    key,
                    default
                )
            )

        except Exception:

            return float(
                default
            )

    def calculate(
        self,
        equity_state
    ):

        if not isinstance(
            equity_state,
            dict
        ):

            equity_state = {}

        peak_equity = self._safe_value(
            equity_state,
            "peak_equity"
        )

        current_equity = self._safe_value(
            equity_state,
            "equity"
        )

        max_drawdown = self._safe_value(
            equity_state,
            "max_drawdown"
        )

        current_drawdown = self._safe_value(
            equity_state,
            "drawdown"
        )

        if self.recovery_engine is not None:

            try:

                if hasattr(
                    self.recovery_engine,
                    "current_state"
                ):

                    recovery_state = (
                        self.recovery_engine.current_state()
                    )

                    if isinstance(
                        recovery_state,
                        dict
                    ):

                        return recovery_state

            except Exception:

                pass

        if max_drawdown <= 0:

            recovery_percent = 100.0

            status = (
                "FULLY RECOVERED"
            )

        else:

            recovered_amount = (
                max_drawdown
                -
                current_drawdown
            )

            recovery_percent = (
                recovered_amount
                /
                max_drawdown
            ) * 100.0

            recovery_percent = max(
                0.0,
                min(
                    100.0,
                    recovery_percent
                )
            )

            if recovery_percent >= 100.0:

                status = (
                    "FULLY RECOVERED"
                )

            elif recovery_percent > 0.0:

                status = (
                    "RECOVERING"
                )

            else:

                status = (
                    "DRAWDOWN"
                )

        return {

            "equity":
                current_equity,

            "peak_equity":
                peak_equity,

            "max_drawdown":
                max_drawdown,

            "current_drawdown":
                current_drawdown,

            "recovery_percent":
                round(
                    recovery_percent,
                    2
                ),

            "recovery_status":
                status

        }