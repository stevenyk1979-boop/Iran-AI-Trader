"""
Iran AI Trader V2.0
Technical Analysis Engine
"""

from statistics import mean, stdev


class TechnicalAnalysis:

    def sample_data(self):

        return [
            100, 101, 102, 103, 104,
            106, 108, 107, 110, 112,
            113, 115, 117, 118, 120,
            122, 121, 123, 124, 126
        ]

    def sma(self, prices, period):

        if len(prices) < period:
            return None

        return round(mean(prices[-period:]), 2)

    def ema(self, prices, period):

        if len(prices) < period:
            return None

        multiplier = 2 / (period + 1)

        ema = prices[0]

        for price in prices[1:]:
            ema = (price - ema) * multiplier + ema

        return round(ema, 2)

    def rsi(self, prices, period=14):

        if len(prices) <= period:
            return None

        gains = []
        losses = []

        for i in range(1, len(prices)):

            change = prices[i] - prices[i - 1]

            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))

        avg_gain = mean(gains[-period:])
        avg_loss = mean(losses[-period:])

        if avg_loss == 0:
            return 100

        rs = avg_gain / avg_loss

        return round(100 - (100 / (1 + rs)), 2)

    def macd(self, prices):

        ema12 = self.ema(prices, 12)
        ema26 = self.ema(prices, 20)

        if ema12 is None or ema26 is None:
            return None

        return round(ema12 - ema26, 2)

    def bollinger(self, prices, period=20):

        if len(prices) < period:
            return None

        data = prices[-period:]

        middle = mean(data)

        sd = stdev(data)

        upper = middle + (2 * sd)
        lower = middle - (2 * sd)

        return (
            round(lower, 2),
            round(middle, 2),
            round(upper, 2),
        )