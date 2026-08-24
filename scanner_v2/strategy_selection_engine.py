"""
Iran AI Trader Professional

Scanner V2

Sprint52

Strategy Selection Engine

Selects qualified strategies from
ranked strategy candidates.

Selection is based on:

Strategy Score
Strategy Quality
Risk
Performance

IMPORTANT:
No broker connection.
No real order execution.
"""


class StrategySelectionEngine:

    def __init__(
        self,
        minimum_score=60.0,
        maximum_drawdown_percent=20.0
    ):

        self.minimum_score = float(
            minimum_score
        )

        self.maximum_drawdown_percent = float(
            maximum_drawdown_percent
        )

        self.selected = []

    # -------------------------------------------------
    # Qualification
    # -------------------------------------------------

    def is_qualified(
        self,
        strategy
    ):

        if not isinstance(
            strategy,
            dict
        ):

            return False

        try:

            score = float(
                strategy.get(
                    "score",
                    strategy.get(
                        "strategy_quality_score",
                        0.0
                    )
                )
            )

        except Exception:

            return False

        if score < self.minimum_score:

            return False

        performance = strategy.get(
            "performance",
            {}
        )

        if not isinstance(
            performance,
            dict
        ):

            performance = {}

        try:

            max_drawdown = float(
                performance.get(
                    "max_drawdown_percent",
                    0.0
                )
            )

        except Exception:

            return False

        if (
            max_drawdown
            > self.maximum_drawdown_percent
        ):

            return False

        status = str(
            strategy.get(
                "status",
                strategy.get(
                    "strategy_quality_status",
                    ""
                )
            )
        ).upper()

        if status in (
            "DANGEROUS",
            "WEAK"
        ):

            return False

        return True

    # -------------------------------------------------
    # Select
    # -------------------------------------------------

    def select(
        self,
        strategies
    ):

        if not isinstance(
            strategies,
            list
        ):

            self.selected = []

            return []

        selected = []

        for strategy in strategies:

            if self.is_qualified(
                strategy
            ):

                selected.append(
                    dict(strategy)
                )

        self.selected = selected

        return selected

    # -------------------------------------------------
    # Select top
    # -------------------------------------------------

    def select_top(
        self,
        strategies,
        limit=5
    ):

        selected = self.select(
            strategies
        )

        try:

            limit = int(
                limit
            )

        except Exception:

            limit = 5

        if limit < 1:

            return []

        return selected[
            :limit
        ]

    # -------------------------------------------------
    # Current selection
    # -------------------------------------------------

    def current_selection(self):

        return list(
            self.selected
        )