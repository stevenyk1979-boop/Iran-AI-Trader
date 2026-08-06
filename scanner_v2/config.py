"""
Iran AI Trader Professional

Scanner V2

Sprint44-07

Scanner Configuration
"""


class ScannerConfig:


    def __init__(self):

        self.test_mode = True

        self.data_source = "fake"

        self.minimum_candles = 20

        self.minimum_score = 70



    def is_test_mode(self):

        return self.test_mode



    def get_data_source(self):

        return self.data_source



    def get_minimum_candles(self):

        return self.minimum_candles



    def get_minimum_score(self):

        return self.minimum_score