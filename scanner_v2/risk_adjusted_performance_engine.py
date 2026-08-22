"""
Iran AI Trader Professional

Scanner V2

Sprint48

Risk-Adjusted Performance Engine

Evaluates strategy quality using:

- Return
- Win Rate
- Profit Factor
- Maximum Drawdown
- Recovery

Output:

STRONG
ACCEPTABLE
WEAK
DANGEROUS
"""


class RiskAdjustedPerformanceEngine:

    def __init__(
        self,
        strong_return=15.0,
        acceptable_return=8.0,
        strong_profit_factor=2.0,
        acceptable_profit_factor=1.2,
        strong_max_drawdown=10.0,
        dangerous_max_drawdown=25.0,
        strong_recovery=75.0
    ):

        self.strong_return = float(
            strong_return
        )

        self.acceptable_return = float(
            acceptable_return
        )

        self.strong_profit_factor = float(
            strong_profit_factor
        )

        self.acceptable_profit_factor = float(
            acceptable_profit_factor
        )

        self.strong_max_drawdown = float(
            strong_max_drawdown
        )

        self.dangerous_max_drawdown = float(
            dangerous_max_drawdown
        )

        self.strong_recovery = float(
            strong_recovery
        )

    # -------------------------------------------------
    # Normalize input
    # -------------------------------------------------

    def _value(
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

    # -------------------------------------------------
    # Evaluate
    # -------------------------------------------------

    def evaluate(
        self,
        performance
    ):

        if not isinstance(
            performance,
            dict
        ):

            performance = {}

        return_percent = self._value(
            performance,
            "return_percent"
        )

        win_rate = self._value(
            performance,
            "win_rate_percent"
        )

        profit_factor = self._value(
            performance,
            "profit_factor"
        )

        max_drawdown_percent = self._value(
            performance,
            "max_drawdown_percent"
        )

        recovery_percent = self._value(
            performance,
            "recovery_percent"
        )

        # -------------------------------------------------
        # Dangerous condition
        # -------------------------------------------------

        if (
            max_drawdown_percent >=
            self.dangerous_max_drawdown
        ):

            return {

                "status": "DANGEROUS",

                "return_percent":
                    return_percent,

                "win_rate_percent":
                    win_rate,

                "profit_factor":
                    profit_factor,

                "max_drawdown_percent":
                    max_drawdown_percent,

                "recovery_percent":
                    recovery_percent,

                "reason":
                    "MAX_DRAWDOWN_TOO_HIGH"

            }

        # -------------------------------------------------
        # Strong condition
        # -------------------------------------------------

        if (

            return_percent >=
            self.strong_return

            and

            profit_factor >=
            self.strong_profit_factor

            and

            max_drawdown_percent <=
            self.strong_max_drawdown

            and

            recovery_percent >=
            self.strong_recovery

        ):

            return {

                "status": "STRONG",

                "return_percent":
                    return_percent,

                "win_rate_percent":
                    win_rate,

                "profit_factor":
                    profit_factor,

                "max_drawdown_percent":
                    max_drawdown_percent,

                "recovery_percent":
                    recovery_percent,

                "reason":
                    "STRONG_RISK_ADJUSTED_PERFORMANCE"

            }

        # -------------------------------------------------
        # Acceptable condition
        # -------------------------------------------------

        if (

            return_percent >=
            self.acceptable_return

            and

            profit_factor >=
            self.acceptable_profit_factor

            and

            max_drawdown_percent <
            self.dangerous_max_drawdown

        ):

            return {

                "status": "ACCEPTABLE",

                "return_percent":
                    return_percent,

                "win_rate_percent":
                    win_rate,

                "profit_factor":
                    profit_factor,

                "max_drawdown_percent":
                    max_drawdown_percent,

                "recovery_percent":
                    recovery_percent,

                "reason":
                    "ACCEPTABLE_RISK_ADJUSTED_PERFORMANCE"

            }

        # -------------------------------------------------
        # Weak
        # -------------------------------------------------

        return {

            "status": "WEAK",

            "return_percent":
                return_percent,

            "win_rate_percent":
                win_rate,

            "profit_factor":
                profit_factor,

            "max_drawdown_percent":
                max_drawdown_percent,

            "recovery_percent":
                recovery_percent,

            "reason":
                "WEAK_RISK_ADJUSTED_PERFORMANCE"

        }