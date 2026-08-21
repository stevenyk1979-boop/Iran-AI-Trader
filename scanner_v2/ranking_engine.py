"""
Iran AI Trader Professional

Scanner V2

Sprint44-37

Ranking Engine - Market Regime Integrated
"""

from scanner_v2.config import ScannerConfig
from scanner_v2.ranking_breakdown import RankingBreakdown

from scanner_v2.scoring.price_score import PriceScoreEngine
from scanner_v2.scoring.direction_score import DirectionScoreEngine
from scanner_v2.scoring.strength_score import StrengthScoreEngine
from scanner_v2.scoring.consistency_score import ConsistencyScoreEngine
from scanner_v2.scoring.trend_score import TrendScoreEngine
from scanner_v2.scoring.momentum_score import MomentumScoreEngine


class RankingEngine:

    def __init__(
        self,
        config=None
    ):

        self.config = (
            config
            or ScannerConfig()
        )

        self.price_engine = PriceScoreEngine(
            config=self.config
        )

        self.direction_engine = DirectionScoreEngine(
            config=self.config
        )

        self.strength_engine = StrengthScoreEngine(
            config=self.config
        )

        self.consistency_engine = ConsistencyScoreEngine(
            config=self.config
        )

        self.trend_engine = TrendScoreEngine(
            config=self.config
        )

        self.momentum_engine = MomentumScoreEngine(
            config=self.config
        )

        self.results = []


    def analyze(
        self,
        history,
        symbol,
        market_regime=None
    ):

        try:

            errors = (
                self.config.validate_ranking_weights()
            )

            if errors:

                raise Exception(
                    "; ".join(errors)
                )


            if history is None:

                raise Exception(
                    "No history"
                )


            prices = history.close_prices()


            if prices is None:

                raise Exception(
                    "No prices"
                )


            minimum_candles = (
                self.config.get_minimum_candles()
            )


            if len(prices) < minimum_candles:

                raise Exception(
                    "Not enough candles"
                )


            # ---------------------------------------------
            # Base scoring engines
            # ---------------------------------------------

            price_score = (
                self.price_engine.calculate(
                    prices
                )
            )


            direction_score = (
                self.direction_engine.calculate(
                    prices
                )
            )


            strength_score = (
                self.strength_engine.calculate(
                    prices
                )
            )


            consistency_score = (
                self.consistency_engine.calculate(
                    prices
                )
            )


            trend_score = (
                self.trend_engine.calculate(
                    direction_score,
                    strength_score,
                    consistency_score
                )
            )


            momentum_score = (
                self.momentum_engine.calculate(
                    prices
                )
            )


            # ---------------------------------------------
            # Ranking breakdown
            # ---------------------------------------------

            breakdown = RankingBreakdown()


            breakdown.add(
                name="price",
                score=price_score,
                weight=self.config.get_price_weight()
            )


            breakdown.add(
                name="trend",
                score=trend_score,
                weight=self.config.get_trend_weight()
            )


            breakdown.add(
                name="momentum",
                score=momentum_score,
                weight=self.config.get_momentum_weight()
            )


            base_score = (
                breakdown.final_score()
            )


            # ---------------------------------------------
            # Market Regime adjustment
            # ---------------------------------------------

            regime_multiplier = (
                self.get_regime_multiplier(
                    market_regime
                )
            )


            score = (
                base_score
                * regime_multiplier
            )


            # Keep score inside 0-100
            score = max(
                0,
                min(
                    100,
                    round(score, 2)
                )
            )


            ranking_breakdown = (
                breakdown.to_dict()
            )


            price_contribution = (
                ranking_breakdown[
                    "price"
                ][
                    "contribution"
                ]
            )


            trend_contribution = (
                ranking_breakdown[
                    "trend"
                ][
                    "contribution"
                ]
            )


            momentum_contribution = (
                ranking_breakdown[
                    "momentum"
                ][
                    "contribution"
                ]
            )


            price_weight = (
                self.config.get_price_weight()
            )

            trend_weight = (
                self.config.get_trend_weight()
            )

            momentum_weight = (
                self.config.get_momentum_weight()
            )


            result = {

                "symbol": symbol,

                "score": score,

                "base_score": round(
                    base_score,
                    2
                ),

                "market_regime": (
                    market_regime
                ),

                "regime_multiplier": (
                    regime_multiplier
                ),

                "price_score": price_score,

                "trend_score": trend_score,

                "momentum_score": momentum_score,

                "direction_score": direction_score,

                "strength_score": strength_score,

                "consistency_score": consistency_score,

                "price_weight": price_weight,

                "trend_weight": trend_weight,

                "momentum_weight": momentum_weight,

                "price_contribution": (
                    price_contribution
                ),

                "trend_contribution": (
                    trend_contribution
                ),

                "momentum_contribution": (
                    momentum_contribution
                ),

                "ranking_breakdown": (
                    ranking_breakdown
                ),

                "decision": (
                    self.decision(
                        score
                    )
                )
            }


            self.results.append(
                result
            )


            return result


        except Exception as error:

            return {

                "symbol": symbol,

                "score": 0,

                "base_score": 0,

                "market_regime": (
                    market_regime
                ),

                "regime_multiplier": 1.0,

                "decision": "FAILED",

                "error": str(error)

            }


    def get_regime_multiplier(
        self,
        market_regime
    ):

        """
        Market regime multiplier.

        Stronger market conditions allow
        stronger ranking scores.

        The multiplier is deliberately
        conservative in V2.
        """

        multipliers = {

            "STRONG BULL": 1.05,

            "BULL": 1.03,

            "EARLY BULL": 1.01,

            "SIDEWAYS": 1.00,

            "BEAR": 0.97,

            "STRONG BEAR": 0.94

        }


        return multipliers.get(
            market_regime,
            1.00
        )


    def decision(
        self,
        score
    ):

        minimum_score = (
            self.config.get_minimum_score()
        )


        if score >= 80:

            return "STRONG WATCH"


        if score >= minimum_score:

            return "WATCH"


        return "IGNORE"