"""
Iran AI Trader Professional
Multi Time Frame Analyzer
"""


class MultiTimeFrameAnalyzer:

    def __init__(self, technical_analysis):

        self.ta = technical_analysis

    def analyze(self, prices):

        """
        Analyze one timeframe.
        """

        bands = self.ta.bollinger(prices)

        return {

            "sma": self.ta.sma(prices, 10),

            "ema": self.ta.ema(prices, 10),

            "rsi": self.ta.rsi(prices),

            "macd": self.ta.macd(prices),

            "bollinger": bands,

            "close": prices[-1]

        }

    def analyze_all(self, history):

        """
        Placeholder for future multi-timeframe support.
        """

        prices = history.close_prices()

        daily = self.analyze(prices)

        return {

            "weekly": daily,

            "daily": daily,

            "4h": daily,

            "1h": daily,

            "15m": daily

        }