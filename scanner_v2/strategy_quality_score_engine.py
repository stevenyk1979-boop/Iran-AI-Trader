"""
Iran AI Trader Professional

Scanner V2

Sprint49

Strategy Quality Score Engine
"""


class StrategyQualityScoreEngine:

    def __init__(
        self,
        target_return=20.0,
        target_win_rate=60.0,
        target_profit_factor=2.0,
        target_max_drawdown=10.0,
        target_recovery=100.0,
        dangerous_max_drawdown=25.0
    ):

        self.target_return = float(target_return)
        self.target_win_rate = float(target_win_rate)
        self.target_profit_factor = float(target_profit_factor)
        self.target_max_drawdown = float(target_max_drawdown)
        self.target_recovery = float(target_recovery)
        self.dangerous_max_drawdown = float(
            dangerous_max_drawdown
        )

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
            return float(default)

    def _clamp(
        self,
        value,
        minimum=0.0,
        maximum=100.0
    ):

        return max(
            minimum,
            min(
                maximum,
                value
            )
        )

    def return_score(
        self,
        return_percent
    ):

        if self.target_return <= 0:
            return 0.0

        score = (
            return_percent
            /
            self.target_return
        ) * 100

        return round(
            self._clamp(score),
            2
        )

    def win_rate_score(
        self,
        win_rate_percent
    ):

        if self.target_win_rate <= 0:
            return 0.0

        score = (
            win_rate_percent
            /
            self.target_win_rate
        ) * 100

        return round(
            self._clamp(score),
            2
        )

    def profit_factor_score(
        self,
        profit_factor
    ):

        if self.target_profit_factor <= 0:
            return 0.0

        score = (
            profit_factor
            /
            self.target_profit_factor
        ) * 100

        return round(
            self._clamp(score),
            2
        )

    def drawdown_score(
        self,
        max_drawdown_percent
    ):

        if max_drawdown_percent <= 0:
            return 100.0

        if (
            max_drawdown_percent
            >=
            self.dangerous_max_drawdown
        ):
            return 0.0

        score = (
            1.0
            -
            (
                max_drawdown_percent
                /
                self.target_max_drawdown
            )
        ) * 100

        score = max(
            20.0,
            score
        )

        return round(
            self._clamp(score),
            2
        )

    def recovery_score(
        self,
        recovery_percent
    ):

        if self.target_recovery <= 0:
            return 0.0

        score = (
            recovery_percent
            /
            self.target_recovery
        ) * 100

        return round(
            self._clamp(score),
            2
        )

    def classification(
        self,
        score
    ):

        if score >= 85:
            return "EXCELLENT"

        if score >= 70:
            return "STRONG"

        if score >= 50:
            return "ACCEPTABLE"

        if score >= 30:
            return "WEAK"

        return "DANGEROUS"

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

        return_component = (
            self.return_score(
                return_percent
            )
        )

        win_rate_component = (
            self.win_rate_score(
                win_rate
            )
        )

        profit_factor_component = (
            self.profit_factor_score(
                profit_factor
            )
        )

        drawdown_component = (
            self.drawdown_score(
                max_drawdown_percent
            )
        )

        recovery_component = (
            self.recovery_score(
                recovery_percent
            )
        )

        score = (

            return_component * 0.25

            +

            win_rate_component * 0.15

            +

            profit_factor_component * 0.20

            +

            drawdown_component * 0.20

            +

            recovery_component * 0.20

        )

        score = round(
            self._clamp(score),
            2
        )

        status = (
            self.classification(
                score
            )
        )

        return {

            "score": score,

            "status": status,

            "return_score":
                return_component,

            "win_rate_score":
                win_rate_component,

            "profit_factor_score":
                profit_factor_component,

            "drawdown_score":
                drawdown_component,

            "recovery_score":
                recovery_component,

            "return_percent":
                return_percent,

            "win_rate_percent":
                win_rate,

            "profit_factor":
                profit_factor,

            "max_drawdown_percent":
                max_drawdown_percent,

            "recovery_percent":
                recovery_percent

        }