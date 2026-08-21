# `scanner_v2/scoring/momentum_score.py`


"""
Iran AI Trader Professional

Scanner V2

Sprint44-36

Momentum Score Engine
"""


class MomentumScoreEngine:

    def __init__(
        self,
        config=None
    ):

        self.config = config


    # -----------------------------------------------------
    # Calculate momentum score
    # -----------------------------------------------------

    def calculate(
        self,
        prices
    ):

        if prices is None:

            raise ValueError(
                "prices are required"
            )


        if len(prices) < 2:

            raise ValueError(
                "at least 2 prices are required"
            )


        try:

            first_price = float(
                prices[0]
            )

            last_price = float(
                prices[-1]
            )

        except (
            TypeError,
            ValueError
        ):

            raise ValueError(
                "prices must be numeric"
            )


        if first_price <= 0:

            raise ValueError(
                "first price must be > 0"
            )


        # -------------------------------------------------
        # Percentage momentum
        # -------------------------------------------------

        momentum_percent = (

            (
                last_price
                -
                first_price
            )
            /
            first_price
        ) * 100.0


        # -------------------------------------------------
        # Normalize momentum to 0 - 100
        #
        # +20% or more  -> 100
        #   0%          -> 50
        # -20% or less  -> 0
        # -------------------------------------------------

        score = (

            50.0
            +
            (
                momentum_percent
                *
                2.5
            )

        )


        score = max(
            0.0,
            min(
                100.0,
                score
            )
        )


        return round(
            score,
            2
        )

