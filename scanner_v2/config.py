
"""
Iran AI Trader Professional

Scanner V2

Sprint44-28

Scanner Configuration
"""


class ScannerConfig:

    def __init__(self):

        self.test_mode = True

        self.data_source = "fake"

        self.minimum_candles = 20

        self.minimum_score = 70

        # Ranking weights

        self.price_weight = 0.60

        self.trend_weight = 0.40


    def is_test_mode(self):

        return self.test_mode


    def get_data_source(self):

        return self.data_source


    def get_minimum_candles(self):

        return self.minimum_candles


    def get_minimum_score(self):

        return self.minimum_score


    def get_price_weight(self):

        return self.price_weight


    def get_trend_weight(self):

        return self.trend_weight


    def validate_ranking_weights(self):

        if self.price_weight < 0:

            return False


        if self.trend_weight < 0:

            return False


        if (
            self.price_weight
            +
            self.trend_weight
        ) <= 0:

            return False


        return True

