# `scanner_v2/ranking_breakdown.py`


"""
Iran AI Trader Professional

Scanner V2

Sprint44-35

Ranking Breakdown - Generic Multi-Engine Support
"""


class RankingBreakdown:

    def __init__(
        self,
        price_score=None,
        trend_score=None,
        price_weight=None,
        trend_weight=None
    ):

        self.components = {}

        # -------------------------------------------------
        # Backward compatibility
        # -------------------------------------------------

        if (
            price_score is not None
            and price_weight is not None
        ):

            self.add(
                name="price",
                score=price_score,
                weight=price_weight
            )

        if (
            trend_score is not None
            and trend_weight is not None
        ):

            self.add(
                name="trend",
                score=trend_score,
                weight=trend_weight
            )


    # -----------------------------------------------------
    # Add generic ranking component
    # -----------------------------------------------------

    def add(
        self,
        name,
        score,
        weight
    ):

        if not name:

            raise ValueError(
                "ranking component name is required"
            )


        if name in self.components:

            raise ValueError(
                f"duplicate ranking component: {name}"
            )


        if score is None:

            raise ValueError(
                "ranking component score is required"
            )


        if weight is None:

            raise ValueError(
                "ranking component weight is required"
            )


        # -------------------------------------------------
        # Validate score
        # -------------------------------------------------

        try:

            numeric_score = float(
                score
            )

        except (
            TypeError,
            ValueError
        ):

            raise ValueError(
                "ranking component score must be numeric"
            )


        # -------------------------------------------------
        # Validate weight
        # -------------------------------------------------

        try:

            numeric_weight = float(
                weight
            )

        except (
            TypeError,
            ValueError
        ):

            raise ValueError(
                "ranking component weight must be numeric"
            )


        if numeric_weight < 0:

            raise ValueError(
                "ranking component weight must be >= 0"
            )


        # -------------------------------------------------
        # Store component
        # -------------------------------------------------

        self.components[name] = {

            "score": round(
                numeric_score,
                2
            ),

            "weight": numeric_weight

        }


    # -----------------------------------------------------
    # Total ranking weight
    # -----------------------------------------------------

    def weight_sum(self):

        return sum(

            component["weight"]

            for component
            in self.components.values()

        )


    # -----------------------------------------------------
    # Contribution of one component
    # -----------------------------------------------------

    def contribution(
        self,
        name
    ):

        if name not in self.components:

            raise KeyError(
                f"unknown ranking component: {name}"
            )


        component = (
            self.components[name]
        )


        return round(

            component["score"]
            *
            component["weight"],

            2

        )


    # -----------------------------------------------------
    # Final normalized weighted score
    # -----------------------------------------------------

    def final_score(self):

        total_weight = (
            self.weight_sum()
        )


        if total_weight <= 0:

            raise ValueError(
                "ranking weight sum must be > 0"
            )


        total_contribution = sum(

            self.contribution(
                name
            )

            for name
            in self.components

        )


        return round(

            total_contribution
            /
            total_weight,

            2

        )


    # -----------------------------------------------------
    # Convert to dictionary
    # -----------------------------------------------------

    def to_dict(self):

        result = {}


        for (
            name,
            component
        ) in self.components.items():

            result[name] = {

                "score": (
                    component["score"]
                ),

                "weight": (
                    component["weight"]
                ),

                "contribution": (
                    self.contribution(
                        name
                    )
                )

            }


        result["final_score"] = (
            self.final_score()
        )


        return result

