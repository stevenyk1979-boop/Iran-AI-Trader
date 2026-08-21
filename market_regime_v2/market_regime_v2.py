# market_regime_v2.py


"""
Iran AI Trader Professional

Market Regime V2
Core Engine
Sprint38 Package Version
"""

from .trend_engine import TrendEngine
from .breadth_engine import BreadthEngine
from .liquidity_engine import LiquidityEngine
from .volatility_engine import VolatilityEngine
from .macro_engine import MacroEngine

from .regime_config import (
    TREND_WEIGHT,
    BREADTH_WEIGHT,
    LIQUIDITY_WEIGHT,
    VOLATILITY_WEIGHT,
    MACRO_WEIGHT,
    STRONG_BULL_THRESHOLD,
    BULL_THRESHOLD,
    EARLY_BULL_THRESHOLD,
    SIDEWAYS_THRESHOLD,
    BEAR_THRESHOLD,
)


class MarketRegimeV2:

    def __init__(self):

        self.trend = TrendEngine()
        self.breadth = BreadthEngine()
        self.liquidity = LiquidityEngine()
        self.volatility = VolatilityEngine()
        self.macro = MacroEngine()

    # -------------------------------------

    def classify_regime(self, score):

        if score >= STRONG_BULL_THRESHOLD:
            return "STRONG BULL"

        elif score >= BULL_THRESHOLD:
            return "BULL"

        elif score >= EARLY_BULL_THRESHOLD:
            return "EARLY BULL"

        elif score >= SIDEWAYS_THRESHOLD:
            return "SIDEWAYS"

        elif score >= BEAR_THRESHOLD:
            return "BEAR"

        else:
            return "STRONG BEAR"

    # -------------------------------------

    def calculate(self, data):

        trend_score = self.trend.calculate(
            data["price"],
            data["ema20"],
            data["ema50"],
            data["ema100"],
            data["ema50_prev"],
        )

        breadth_score = self.breadth.calculate(
            data["positive"],
            data["negative"],
            data["unchanged"],
        )

        liquidity_score = self.liquidity.calculate(
            data["volume"],
            data["avg_volume"],
            data["value"],
            data["avg_value"],
            data["money_flow"],
        )

        volatility_score = self.volatility.calculate(
            data["atr_percent"],
            data["market_volatility"],
            data["drawdown"],
        )

        macro_score = self.macro.calculate(
            data["index_change"],
            data["equal_change"],
            data["money_flow"],
        )

        # Weights are percentage-based.
        # Final score must remain in the 0-100 range.
        final_score = (
            trend_score * TREND_WEIGHT
            + breadth_score * BREADTH_WEIGHT
            + liquidity_score * LIQUIDITY_WEIGHT
            + volatility_score * VOLATILITY_WEIGHT
            + macro_score * MACRO_WEIGHT
        ) / 100

        regime = self.classify_regime(
            final_score
        )

        return {
            "regime": regime,
            "score": round(final_score, 2),
            "trend": round(trend_score, 2),
            "breadth": round(breadth_score, 2),
            "liquidity": round(liquidity_score, 2),
            "volatility": round(volatility_score, 2),
            "macro": round(macro_score, 2),
        }

