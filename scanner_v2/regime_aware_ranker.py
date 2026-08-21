"""
Iran AI Trader Professional

Scanner V2

Regime-Aware Ranking Engine
Sprint45-01

Adjusts stock ranking according to market regime.
"""


class RegimeAwareRanker:

    REGIME_MULTIPLIERS = {
        "STRONG BULL": 1.10,
        "BULL": 1.05,
        "EARLY BULL": 1.02,
        "SIDEWAYS": 1.00,
        "BEAR": 0.90,
        "STRONG BEAR": 0.80,
        "UNKNOWN": 1.00,
    }

    def __init__(self):

        self.results = []


    # -------------------------------------------------
    # Get regime multiplier
    # -------------------------------------------------

    def get_multiplier(self, regime):

        return self.REGIME_MULTIPLIERS.get(
            regime,
            1.00
        )


    # -------------------------------------------------
    # Adjust one score
    # -------------------------------------------------

    def adjust(
        self,
        score,
        regime
    ):

        try:

            score = float(score)

            multiplier = (
                self.get_multiplier(
                    regime
                )
            )

            adjusted_score = (
                score * multiplier
            )

            adjusted_score = max(
                0,
                min(
                    100,
                    adjusted_score
                )
            )

            result = {

                "original_score": round(
                    score,
                    2
                ),

                "regime": regime,

                "multiplier": multiplier,

                "adjusted_score": round(
                    adjusted_score,
                    2
                )
            }

            return result


        except Exception as error:

            return {

                "original_score": 0,

                "regime": regime,

                "multiplier": 1.00,

                "adjusted_score": 0,

                "error": str(error)
            }


    # -------------------------------------------------
    # Rank complete result list
    # -------------------------------------------------

    def rank(
        self,
        results
    ):

        self.results = []

        if results is None:

            return []


        for item in results:

            try:

                score = float(
                    item.get(
                        "score",
                        0
                    )
                )

                regime = item.get(
                    "market_regime",
                    "UNKNOWN"
                )

                adjusted = (
                    self.adjust(
                        score,
                        regime
                    )
                )

                ranked_item = dict(
                    item
                )

                ranked_item[
                    "regime_multiplier"
                ] = adjusted[
                    "multiplier"
                ]

                ranked_item[
                    "regime_adjusted_score"
                ] = adjusted[
                    "adjusted_score"
                ]

                self.results.append(
                    ranked_item
                )


            except Exception as error:

                ranked_item = dict(
                    item
                )

                ranked_item[
                    "regime_multiplier"
                ] = 1.00

                ranked_item[
                    "regime_adjusted_score"
                ] = 0

                ranked_item[
                    "regime_adjustment_error"
                ] = str(error)

                self.results.append(
                    ranked_item
                )


        # -------------------------------------------------
        # Highest adjusted score first
        # -------------------------------------------------

        self.results.sort(
            key=lambda item: item.get(
                "regime_adjusted_score",
                0
            ),
            reverse=True
        )


        # -------------------------------------------------
        # Add ranking position
        # -------------------------------------------------

        for index, item in enumerate(
            self.results,
            start=1
        ):

            item["rank"] = index


        return self.results