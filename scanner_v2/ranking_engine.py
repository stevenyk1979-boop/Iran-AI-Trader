
"""
Iran AI Trader Professional

Scanner V2

Sprint44-29

Ranking Engine - Detailed Ranking Weight Validation
"""

from scanner_v2.config import ScannerConfig

from scanner_v2.scoring.price_score import PriceScoreEngine
from scanner_v2.scoring.direction_score import DirectionScoreEngine
from scanner_v2.scoring.strength_score import StrengthScoreEngine
from scanner_v2.scoring.consistency_score import ConsistencyScoreEngine
from scanner_v2.scoring.trend_score import TrendScoreEngine


class RankingEngine:

    def __init__(self, config=None):

        self.config = config or ScannerConfig()

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

        self.results = []


    def analyze(
        self,
        history,
        symbol
    ):

        try:

            # Validate ranking weights

            errors = self.config.validate_ranking_weights()

            if errors:

                raise Exception(
                    "; ".join(errors)
                )


            # Validate history

            if history is None:

                raise Exception(
                    "No history"
                )


            prices = history.close_prices()


            if prices is None:

                raise Exception(
                    "No prices"
                )


            # Validate minimum candles

            if len(prices) < self.config.get_minimum_candles():

                raise Exception(
                    "Not enough candles"
                )


            # Price score

            price_score = self.price_engine.calculate(
                prices
            )


            # Direction score

            direction_score = self.direction_engine.calculate(
                prices
            )


            # Strength score

            strength_score = self.strength_engine.calculate(
                prices
            )


            # Consistency score

            consistency_score = self.consistency_engine.calculate(
                prices
            )


            # Trend score

            trend_score = self.trend_engine.calculate(
                direction_score,
                strength_score,
                consistency_score
            )


            # Ranking weights

            price_weight = self.config.get_price_weight()

            trend_weight = self.config.get_trend_weight()


            weight_sum = (
                price_weight
                +
                trend_weight
            )


            if weight_sum <= 0:

                raise Exception(
                    "ranking weight sum must be > 0"
                )


            # Final score

            score = (

                (
                    price_score
                    *
                    price_weight
                )

                +

                (
                    trend_score
                    *
                    trend_weight
                )

            ) / weight_sum


            score = round(
                score,
                2
            )


            # Final result

            result = {

                "symbol": symbol,

                "score": score,

                "price_score": price_score,

                "trend_score": trend_score,

                "direction_score": direction_score,

                "strength_score": strength_score,

                "consistency_score": consistency_score,

                "price_weight": price_weight,

                "trend_weight": trend_weight,

                "decision": self.decision(
                    score
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

                "decision": "FAILED",

                "error": str(error)

            }


    def decision(
        self,
        score
    ):

        minimum_score = self.config.get_minimum_score()


        if score >= 80:

            return "STRONG WATCH"


        if score >= minimum_score:

            return "WATCH"


        return "IGNORE"

