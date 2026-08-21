"""
Iran AI Trader Professional

Scanner V2

Sprint45-03

Final Signal Engine

Converts regime-aware candidate results
into a final trading/watch signal.
"""


class FinalSignalEngine:

    def __init__(self):

        self.results = []


    # -------------------------------------------------
    # Generate signal for one candidate
    # -------------------------------------------------

    def generate(
        self,
        item
    ):

        try:

            score = float(
                item.get(
                    "regime_adjusted_score",
                    item.get(
                        "final_watchlist_score",
                        item.get(
                            "score",
                            0
                        )
                    )
                )
            )

            candidate_score = float(
                item.get(
                    "candidate_score",
                    0
                )
            )

            status = item.get(
                "status",
                item.get(
                    "candidate_status",
                    "IGNORE"
                )
            )

            regime = item.get(
                "market_regime",
                item.get(
                    "regime",
                    "UNKNOWN"
                )
            )


            # -----------------------------------------
            # Final decision thresholds
            # -----------------------------------------

            if (
                score >= 90
                and candidate_score >= 80
                and status == "READY"
            ):

                signal = "STRONG BUY"


            elif (
                score >= 80
                and candidate_score >= 65
                and status in (
                    "READY",
                    "EARLY"
                )
            ):

                signal = "BUY"


            elif (
                score >= 65
                and candidate_score >= 50
            ):

                signal = "WATCH"


            else:

                signal = "IGNORE"


            return {

                "symbol": item.get(
                    "symbol"
                ),

                "score": round(
                    score,
                    2
                ),

                "candidate_score": round(
                    candidate_score,
                    2
                ),

                "regime": regime,

                "candidate_status": status,

                "signal": signal

            }


        except Exception as error:

            return {

                "symbol": (
                    item.get(
                        "symbol"
                    )
                    if item
                    else None
                ),

                "score": 0,

                "candidate_score": 0,

                "regime": "UNKNOWN",

                "candidate_status": "IGNORE",

                "signal": "IGNORE",

                "error": str(
                    error
                )

            }


    # -------------------------------------------------
    # Generate signals for complete list
    # -------------------------------------------------

    def evaluate(
        self,
        results
    ):

        self.results = []

        if results is None:

            return []


        if not isinstance(
            results,
            list
        ):

            return []


        for item in results:

            if not isinstance(
                item,
                dict
            ):

                continue


            result = self.generate(
                item
            )

            self.results.append(
                result
            )


        # Strongest signals first

        signal_priority = {

            "STRONG BUY": 4,

            "BUY": 3,

            "WATCH": 2,

            "IGNORE": 1

        }


        self.results.sort(
            key=lambda item: (
                signal_priority.get(
                    item.get(
                        "signal",
                        "IGNORE"
                    ),
                    1
                ),
                item.get(
                    "score",
                    0
                )
            ),
            reverse=True
        )


        # Final rank

        for index, item in enumerate(
            self.results,
            start=1
        ):

            item[
                "signal_rank"
            ] = index


        return self.results


    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(self):

        return {

            "total": len(
                self.results
            ),

            "strong_buy": len(
                [
                    item
                    for item in self.results
                    if item.get(
                        "signal"
                    )
                    == "STRONG BUY"
                ]
            ),

            "buy": len(
                [
                    item
                    for item in self.results
                    if item.get(
                        "signal"
                    )
                    == "BUY"
                ]
            ),

            "watch": len(
                [
                    item
                    for item in self.results
                    if item.get(
                        "signal"
                    )
                    == "WATCH"
                ]
            ),

            "ignore": len(
                [
                    item
                    for item in self.results
                    if item.get(
                        "signal"
                    )
                    == "IGNORE"
                ]
            )

        }