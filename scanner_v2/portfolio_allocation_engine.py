"""
Iran AI Trader Professional

Scanner V2

Sprint45-04

Portfolio Allocation Engine

Builds the final portfolio from position-sizing results.

Responsibilities:
- Select eligible positions
- Respect maximum number of positions
- Respect maximum portfolio allocation
- Prevent total allocation from exceeding 100%
- Preserve signal and risk information
- Produce deterministic portfolio ranking
"""


class PortfolioAllocationEngine:

    def __init__(
        self,
        max_positions=5,
        max_total_allocation=100.0
    ):

        self.max_positions = int(
            max_positions
        )

        if self.max_positions <= 0:
            self.max_positions = 5

        self.max_total_allocation = float(
            max_total_allocation
        )

        if self.max_total_allocation <= 0:
            self.max_total_allocation = 100.0

        self.portfolio = []


    # -------------------------------------------------
    # Eligibility
    # -------------------------------------------------

    def is_eligible(self, item):

        if not isinstance(item, dict):
            return False

        signal = item.get(
            "signal",
            "IGNORE"
        )

        risk_status = item.get(
            "risk_status",
            item.get(
                "status",
                "HIGH RISK"
            )
        )

        allocation = item.get(
            "allocation_percent",
            0
        )

        try:

            allocation = float(
                allocation
            )

        except Exception:

            return False

        if signal not in (
            "STRONG BUY",
            "BUY"
        ):
            return False

        if risk_status != "LOW RISK":
            return False

        if allocation <= 0:
            return False

        return True


    # -------------------------------------------------
    # Build portfolio
    # -------------------------------------------------

    def build(self, results):

        self.portfolio = []

        if results is None:
            return []

        if not isinstance(results, list):
            return []

        eligible = []

        for item in results:

            if not self.is_eligible(item):
                continue

            candidate = dict(
                item
            )

            try:

                candidate[
                    "allocation_percent"
                ] = round(
                    float(
                        candidate.get(
                            "allocation_percent",
                            0
                        )
                    ),
                    2
                )

            except Exception:

                continue

            try:

                candidate[
                    "score"
                ] = round(
                    float(
                        candidate.get(
                            "score",
                            0
                        )
                    ),
                    2
                )

            except Exception:

                candidate["score"] = 0

            try:

                candidate[
                    "risk_score"
                ] = round(
                    float(
                        candidate.get(
                            "risk_score",
                            0
                        )
                    ),
                    2
                )

            except Exception:

                candidate["risk_score"] = 0

            eligible.append(
                candidate
            )


        # -------------------------------------------------
        # Ranking priority
        # -------------------------------------------------

        eligible.sort(
            key=lambda item: (
                item.get(
                    "signal"
                ) == "STRONG BUY",

                item.get(
                    "risk_score",
                    0
                ),

                item.get(
                    "score",
                    0
                )
            ),
            reverse=True
        )


        # -------------------------------------------------
        # Select positions
        # -------------------------------------------------

        total_allocation = 0.0

        for item in eligible:

            if len(
                self.portfolio
            ) >= self.max_positions:

                break

            allocation = float(
                item.get(
                    "allocation_percent",
                    0
                )
            )

            remaining = (
                self.max_total_allocation
                - total_allocation
            )

            if remaining <= 0:
                break

            final_allocation = min(
                allocation,
                remaining
            )

            if final_allocation <= 0:
                continue

            item[
                "final_allocation_percent"
            ] = round(
                final_allocation,
                2
            )

            item[
                "portfolio_rank"
            ] = (
                len(self.portfolio)
                + 1
            )

            total_allocation += (
                final_allocation
            )

            self.portfolio.append(
                item
            )


        # -------------------------------------------------
        # Final statistics
        # -------------------------------------------------

        total_allocation = round(
            total_allocation,
            2
        )

        for item in self.portfolio:

            item[
                "portfolio_total_allocation"
            ] = total_allocation

        return self.portfolio


    # -------------------------------------------------
    # Get portfolio
    # -------------------------------------------------

    def get_portfolio(self):

        return list(
            self.portfolio
        )


    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(self):

        total_allocation = round(
            sum(
                float(
                    item.get(
                        "final_allocation_percent",
                        0
                    )
                )
                for item in self.portfolio
            ),
            2
        )

        return {

            "max_positions":
                self.max_positions,

            "positions":
                len(
                    self.portfolio
                ),

            "max_total_allocation":
                self.max_total_allocation,

            "total_allocation":
                total_allocation,

            "remaining_allocation":
                round(
                    self.max_total_allocation
                    - total_allocation,
                    2
                ),

            "symbols": [
                item.get(
                    "symbol"
                )
                for item in self.portfolio
            ]
        }