"""
Iran AI Trader Professional

Scanner V2

Sprint52

Strategy Quality Ranking Engine

Combines:

Strategy Quality Score
        ↓
Strategy Ranking
        ↓
Ranked Strategy Quality

IMPORTANT:
No broker connection.
No real order execution.
"""


from scanner_v2.strategy_ranking_engine import (
    StrategyRankingEngine
)


class StrategyQualityRankingEngine:

    def __init__(self):

        self.ranking_engine = (
            StrategyRankingEngine()
        )

    # -------------------------------------------------
    # Normalize strategy
    # -------------------------------------------------

    def _normalize(
        self,
        strategy
    ):

        if not isinstance(
            strategy,
            dict
        ):

            return None

        result = dict(
            strategy
        )

        if "score" not in result:

            result["score"] = float(
                result.get(
                    "strategy_quality_score",
                    0.0
                )
            )

        if "status" not in result:

            result["status"] = (
                result.get(
                    "strategy_quality_status",
                    "UNKNOWN"
                )
            )

        return result

    # -------------------------------------------------
    # Rank
    # -------------------------------------------------

    def rank(
        self,
        strategies
    ):

        normalized = []

        if not isinstance(
            strategies,
            list
        ):

            return []

        for strategy in strategies:

            item = self._normalize(
                strategy
            )

            if item is not None:

                normalized.append(
                    item
                )

        return self.ranking_engine.rank(
            normalized
        )

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
    # Strategy lookup
    # -------------------------------------------------

    def find_rank(
        self,
        strategies,
        symbol
    ):

        ranked = self.rank(
            strategies
        )

        for item in ranked:

            if item.get(
                "symbol"
            ) == symbol:

                return item

        return None