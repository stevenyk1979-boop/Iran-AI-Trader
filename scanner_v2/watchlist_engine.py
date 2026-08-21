"""
Iran AI Trader Professional

Scanner V2

Sprint45-02

Top-N Watchlist Engine

Selects the highest-ranked symbols after
regime-aware ranking.
"""


class WatchlistEngine:

    def __init__(self, top_n=10):

        self.top_n = int(top_n)

        if self.top_n <= 0:
            self.top_n = 10

        self.watchlist = []

    # -------------------------------------------------
    # Build watchlist
    # -------------------------------------------------

    def build(self, results):

        self.watchlist = []

        if results is None:
            return []

        if not isinstance(results, list):
            return []

        valid_results = []

        for item in results:

            if not isinstance(item, dict):
                continue

            try:

                score = float(
                    item.get(
                        "regime_adjusted_score",
                        item.get("score", 0)
                    )
                )

                ranked_item = dict(item)

                ranked_item[
                    "final_watchlist_score"
                ] = round(
                    score,
                    2
                )

                valid_results.append(
                    ranked_item
                )

            except Exception:

                continue

        # Highest score first
        valid_results.sort(
            key=lambda item: item.get(
                "final_watchlist_score",
                0
            ),
            reverse=True
        )

        # Select Top-N
        self.watchlist = (
            valid_results[:self.top_n]
        )

        # Add watchlist rank
        for index, item in enumerate(
            self.watchlist,
            start=1
        ):

            item["watchlist_rank"] = index

        return self.watchlist

    # -------------------------------------------------
    # Get watchlist
    # -------------------------------------------------

    def get_watchlist(self):

        return list(
            self.watchlist
        )

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(self):

        return {
            "top_n": self.top_n,

            "count": len(
                self.watchlist
            ),

            "symbols": [
                item.get(
                    "symbol"
                )
                for item in self.watchlist
            ]
        }