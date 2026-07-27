"""
Iran AI Trader V2.0
Market Data Model
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class MarketData:
    symbol: str
    date: datetime

    open_price: float
    high_price: float
    low_price: float
    close_price: float

    volume: int
    value: float

    def last_price(self):
        return self.close_price

    def candle_color(self):

        if self.close_price > self.open_price:
            return "GREEN"

        elif self.close_price < self.open_price:
            return "RED"

        return "DOJI"

    def body_size(self):

        return round(
            abs(self.close_price - self.open_price),
            2,
        )

    def candle_range(self):

        return round(
            self.high_price - self.low_price,
            2,
        )

    def is_bullish(self):

        return self.close_price > self.open_price

    def is_bearish(self):

        return self.close_price < self.open_price

    def summary(self):

        return {
            "symbol": self.symbol,
            "last_price": self.last_price(),
            "color": self.candle_color(),
            "body": self.body_size(),
            "range": self.candle_range(),
            "volume": self.volume,
            "value": self.value,
        }