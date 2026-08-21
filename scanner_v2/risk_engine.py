"""
Iran AI Trader Professional

Scanner V2

Sprint45-04

Risk Engine

Evaluates trade risk from:
- final score
- candidate score
- market regime
- entry price
- stop loss
- take profit
"""

class RiskEngine:

    REGIME_RISK = {
        "STRONG BULL": 0.90,
        "BULL": 0.95,
        "EARLY BULL": 0.97,
        "SIDEWAYS": 1.00,
        "BEAR": 1.15,
        "STRONG BEAR": 1.30,
        "UNKNOWN": 1.00,
    }

    def __init__(self):

        self.results = []


    # -------------------------------------------------
    # Regime risk multiplier
    # -------------------------------------------------

    def get_regime_risk(
        self,
        regime
    ):

        return self.REGIME_RISK.get(
            regime,
            1.00
        )


    # -------------------------------------------------
    # Calculate risk/reward
    # -------------------------------------------------

    def calculate_risk_reward(
        self,
        entry_price,
        stop_loss,
        take_profit
    ):

        try:

            entry = float(
                entry_price
            )

            stop = float(
                stop_loss
            )

            target = float(
                take_profit
            )

            if entry <= 0:
                return 0.0

            risk = entry - stop
            reward = target - entry

            if risk <= 0:
                return 0.0

            if reward <= 0:
                return 0.0

            return round(
                reward / risk,
                2
            )

        except Exception:

            return 0.0


    # -------------------------------------------------
    # Calculate risk score
    # -------------------------------------------------

    def calculate_risk_score(
        self,
        score,
        candidate_score,
        regime
    ):

        try:

            score = float(
                score
            )

            candidate_score = float(
                candidate_score
            )

            regime_multiplier = (
                self.get_regime_risk(
                    regime
                )
            )

            # Higher quality scores
            # produce lower risk.

            quality_score = (
                (score * 0.60)
                +
                (candidate_score * 0.40)
            )

            risk_score = (
                quality_score
                / regime_multiplier
            )

            risk_score = max(
                0,
                min(
                    100,
                    risk_score
                )
            )

            return round(
                risk_score,
                2
            )

        except Exception:

            return 0.0


    # -------------------------------------------------
    # Evaluate one trade
    # -------------------------------------------------

    def evaluate(
        self,
        item
    ):

        try:

            score = float(
                item.get(
                    "score",
                    item.get(
                        "regime_adjusted_score",
                        0
                    )
                )
            )

            candidate_score = float(
                item.get(
                    "candidate_score",
                    0
                )
            )

            regime = item.get(
                "regime",
                item.get(
                    "market_regime",
                    "UNKNOWN"
                )
            )

            entry_price = float(
                item.get(
                    "entry_price",
                    0
                )
            )

            stop_loss = float(
                item.get(
                    "stop_loss",
                    0
                )
            )

            take_profit = float(
                item.get(
                    "take_profit",
                    0
                )
            )

            risk_score = (
                self.calculate_risk_score(
                    score,
                    candidate_score,
                    regime
                )
            )

            risk_reward = (
                self.calculate_risk_reward(
                    entry_price,
                    stop_loss,
                    take_profit
                )
            )


            if (
                risk_score >= 85
                and risk_reward >= 2.0
            ):

                risk_status = "LOW RISK"


            elif (
                risk_score >= 70
                and risk_reward >= 1.5
            ):

                risk_status = "MEDIUM RISK"


            else:

                risk_status = "HIGH RISK"


            result = dict(
                item
            )

            result[
                "risk_score"
            ] = risk_score

            result[
                "risk_reward"
            ] = risk_reward

            result[
                "risk_status"
            ] = risk_status

            return result


        except Exception as error:

            result = dict(
                item
            )

            result[
                "risk_score"
            ] = 0

            result[
                "risk_reward"
            ] = 0

            result[
                "risk_status"
            ] = "HIGH RISK"

            result[
                "risk_error"
            ] = str(
                error
            )

            return result


    # -------------------------------------------------
    # Evaluate complete list
    # -------------------------------------------------

    def evaluate_all(
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

            result = self.evaluate(
                item
            )

            self.results.append(
                result
            )


        self.results.sort(
            key=lambda item: (
                item.get(
                    "risk_score",
                    0
                ),
                item.get(
                    "risk_reward",
                    0
                )
            ),
            reverse=True
        )


        for index, item in enumerate(
            self.results,
            start=1
        ):

            item[
                "risk_rank"
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

            "low_risk": len(
                [
                    item
                    for item in self.results
                    if item.get(
                        "risk_status"
                    )
                    == "LOW RISK"
                ]
            ),

            "medium_risk": len(
                [
                    item
                    for item in self.results
                    if item.get(
                        "risk_status"
                    )
                    == "MEDIUM RISK"
                ]
            ),

            "high_risk": len(
                [
                    item
                    for item in self.results
                    if item.get(
                        "risk_status"
                    )
                    == "HIGH RISK"
                ]
            )
        }