"""
Iran AI Trader Professional

Scanner V2

Sprint45-05

Position Sizing Engine

Determines the maximum suggested capital allocation
for a candidate based on signal quality and risk.
"""

class PositionSizingEngine:

    SIGNAL_WEIGHTS = {
        "STRONG BUY": 1.00,
        "BUY": 0.70,
        "WATCH": 0.30,
        "IGNORE": 0.00,
    }

    RISK_WEIGHTS = {
        "LOW RISK": 1.00,
        "MEDIUM RISK": 0.65,
        "HIGH RISK": 0.00,
    }

    def __init__(
        self,
        max_portfolio_percent=20.0
    ):

        self.max_portfolio_percent = float(
            max_portfolio_percent
        )

        if self.max_portfolio_percent <= 0:

            self.max_portfolio_percent = 20.0

        self.results = []


    # -------------------------------------------------
    # Signal multiplier
    # -------------------------------------------------

    def get_signal_weight(
        self,
        signal
    ):

        return self.SIGNAL_WEIGHTS.get(
            signal,
            0.00
        )


    # -------------------------------------------------
    # Risk multiplier
    # -------------------------------------------------

    def get_risk_weight(
        self,
        risk_status
    ):

        return self.RISK_WEIGHTS.get(
            risk_status,
            0.00
        )


    # -------------------------------------------------
    # Calculate allocation percentage
    # -------------------------------------------------

    def calculate_allocation_percent(
        self,
        signal,
        risk_status,
        risk_score
    ):

        try:

            signal_weight = (
                self.get_signal_weight(
                    signal
                )
            )

            risk_weight = (
                self.get_risk_weight(
                    risk_status
                )
            )

            risk_score = float(
                risk_score
            )

            # Normalize risk quality.
            risk_quality = (
                max(
                    0.0,
                    min(
                        100.0,
                        risk_score
                    )
                )
                / 100.0
            )

            allocation = (
                self.max_portfolio_percent
                * signal_weight
                * risk_weight
                * risk_quality
            )

            allocation = max(
                0.0,
                min(
                    self.max_portfolio_percent,
                    allocation
                )
            )

            return round(
                allocation,
                2
            )

        except Exception:

            return 0.0


    # -------------------------------------------------
    # Calculate capital allocation
    # -------------------------------------------------

    def calculate_capital(
        self,
        portfolio_value,
        allocation_percent
    ):

        try:

            portfolio_value = float(
                portfolio_value
            )

            allocation_percent = float(
                allocation_percent
            )

            if portfolio_value <= 0:

                return 0.0

            capital = (
                portfolio_value
                * allocation_percent
                / 100.0
            )

            return round(
                capital,
                2
            )

        except Exception:

            return 0.0


    # -------------------------------------------------
    # Evaluate one candidate
    # -------------------------------------------------

    def evaluate(
        self,
        item,
        portfolio_value
    ):

        try:

            signal = item.get(
                "signal",
                "IGNORE"
            )

            risk_status = item.get(
                "risk_status",
                "HIGH RISK"
            )

            risk_score = float(
                item.get(
                    "risk_score",
                    0
                )
            )

            allocation_percent = (
                self.calculate_allocation_percent(
                    signal,
                    risk_status,
                    risk_score
                )
            )

            allocated_capital = (
                self.calculate_capital(
                    portfolio_value,
                    allocation_percent
                )
            )

            result = dict(
                item
            )

            result[
                "allocation_percent"
            ] = allocation_percent

            result[
                "allocated_capital"
            ] = allocated_capital

            return result

        except Exception as error:

            result = dict(
                item
            )

            result[
                "allocation_percent"
            ] = 0.0

            result[
                "allocated_capital"
            ] = 0.0

            result[
                "position_sizing_error"
            ] = str(
                error
            )

            return result


    # -------------------------------------------------
    # Evaluate complete list
    # -------------------------------------------------

    def evaluate_all(
        self,
        results,
        portfolio_value
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

            result = self.evaluate(
                item,
                portfolio_value
            )

            self.results.append(
                result
            )


        # Highest allocation first

        self.results.sort(
            key=lambda item: (
                item.get(
                    "allocation_percent",
                    0
                ),
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


        # Position sizing rank

        for index, item in enumerate(
            self.results,
            start=1
        ):

            item[
                "position_rank"
            ] = index


        return self.results


    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(self):

        total_capital = sum(
            item.get(
                "allocated_capital",
                0
            )
            for item in self.results
        )

        return {

            "total": len(
                self.results
            ),

            "allocated_capital": round(
                total_capital,
                2
            ),

            "max_portfolio_percent": (
                self.max_portfolio_percent
            ),

            "positions_with_allocation": len(
                [
                    item
                    for item in self.results
                    if item.get(
                        "allocated_capital",
                        0
                    ) > 0
                ]
            )
        }