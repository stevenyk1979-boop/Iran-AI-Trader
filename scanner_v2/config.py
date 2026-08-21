"""
Iran AI Trader Professional

Scanner V2

Sprint44-35

Scanner Configuration
"""


class ScannerConfig:

    def __init__(self):

        # -------------------------------------------------
        # General configuration
        # -------------------------------------------------

        self.test_mode = True

        self.data_source = "fake"

        self.minimum_candles = 20

        self.minimum_score = 70

        # -------------------------------------------------
        # Ranking weights
        # -------------------------------------------------

        self.price_weight = 0.50

        self.trend_weight = 0.30

        self.momentum_weight = 0.20


    # -----------------------------------------------------
    # General getters
    # -----------------------------------------------------

    def is_test_mode(self):

        return self.test_mode


    def get_data_source(self):

        return self.data_source


    def get_minimum_candles(self):

        return self.minimum_candles


    def get_minimum_score(self):

        return self.minimum_score


    # -----------------------------------------------------
    # Ranking weight getters
    # -----------------------------------------------------

    def get_price_weight(self):

        return self.price_weight


    def get_trend_weight(self):

        return self.trend_weight


    def get_momentum_weight(self):

        return self.momentum_weight


    # -----------------------------------------------------
    # Ranking weight validation
    # -----------------------------------------------------

    def validate_ranking_weights(self):

        errors = []


        # -------------------------------------------------
        # Price weight
        # -------------------------------------------------

        try:

            price_weight = float(
                self.price_weight
            )

        except (TypeError, ValueError):

            errors.append(
                "price_weight must be numeric"
            )

            price_weight = 0


        if price_weight < 0:

            errors.append(
                "price_weight must be >= 0"
            )


        # -------------------------------------------------
        # Trend weight
        # -------------------------------------------------

        try:

            trend_weight = float(
                self.trend_weight
            )

        except (TypeError, ValueError):

            errors.append(
                "trend_weight must be numeric"
            )

            trend_weight = 0


        if trend_weight < 0:

            errors.append(
                "trend_weight must be >= 0"
            )


        # -------------------------------------------------
        # Momentum weight
        # -------------------------------------------------

        try:

            momentum_weight = float(
                self.momentum_weight
            )

        except (TypeError, ValueError):

            errors.append(
                "momentum_weight must be numeric"
            )

            momentum_weight = 0


        if momentum_weight < 0:

            errors.append(
                "momentum_weight must be >= 0"
            )


        # -------------------------------------------------
        # Total weight
        # -------------------------------------------------

        weight_sum = (

            price_weight
            +
            trend_weight
            +
            momentum_weight

        )


        if weight_sum <= 0:

            errors.append(
                "ranking weight sum must be > 0"
            )


        return errors


    # -----------------------------------------------------
    # Quick validation
    # -----------------------------------------------------

    def ranking_weights_valid(self):

        return len(
            self.validate_ranking_weights()
        ) == 0