"""
Iran AI Trader Professional

Scanner V2

Sprint52

Strategy Ranking Engine

Ranks strategies by quality score.

IMPORTANT:
No broker connection.
No real order execution.
"""


class StrategyRankingEngine:

    def __init__(self):

        self.results = []

    # -------------------------------------------------
    # Safe score
    # -------------------------------------------------

    def _score(
        self,
        strategy
    ):

        try:

            return float(
                strategy.get(
                    "score",
                    strategy.get(
                        "strategy_quality_score",
                        0.0
                    )
                )
            )

        except Exception:

            return 0.0

    # -------------------------------------------------
    # Ranking
    # -------------------------------------------------

    def rank(
        self,
        strategies
    ):

        if not isinstance(
            strategies,
            list
        ):

            self.results = []

            return []

        ranked = []

        for strategy in strategies:

            if not isinstance(
                strategy,
                dict
            ):

                continue

            item = dict(
                strategy
            )

            item["score"] = (
                self._score(
                    strategy
                )
            )

            ranked.append(
                item
            )

        ranked.sort(
            key=lambda item: item[
                "score"
            ],
            reverse=True
        )

        for index, item in enumerate(
            ranked,
            start=1
        ):

            item["rank"] = index

        self.results = ranked

        return ranked

    # -------------------------------------------------
    # Top strategies
    # -------------------------------------------------

    def top(
        self,
        strategies,
        limit=10
    ):

        ranked = self.rank(
            strategies
        )

        try:

            limit = int(
                limit
            )

        except Exception:

            limit = 10

        if limit < 1:

            return []

        return ranked[
            :limit
        ]

    # -------------------------------------------------
    # Best strategy
    # -------------------------------------------------

    def best(
        self,
        strategies
    ):

        ranked = self.rank(
            strategies
        )

        if not ranked:

            return None

        return ranked[0]

    # -------------------------------------------------
    # Last ranking
    # -------------------------------------------------

    def current_ranking(self):

        return list(
            self.results
        )