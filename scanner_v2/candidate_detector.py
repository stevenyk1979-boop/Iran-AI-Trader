"""
Iran AI Trader Professional

Scanner V2

Candidate Detection Engine

Detects stocks that show early signs of a potential move
before reaching an extreme market condition.
"""


class CandidateDetector:

    def __init__(self):

        self.results = []


    def analyze(self, item):

        try:

            score = float(
                item.get(
                    "regime_adjusted_score",
                    item.get(
                        "score",
                        0
                    )
                )
            )

            strength = float(
                item.get(
                    "strength_score",
                    0
                )
            )

            trend = float(
                item.get(
                    "trend_score",
                    0
                )
            )

            momentum = float(
                item.get(
                    "momentum_score",
                    0
                )
            )

            regime = item.get(
                "market_regime",
                "UNKNOWN"
            )


            # -----------------------------------------
            # Candidate component scores
            # -----------------------------------------

            trend_component = (
                min(
                    100,
                    max(
                        0,
                        trend
                    )
                )
            )

            momentum_component = (
                min(
                    100,
                    max(
                        0,
                        momentum
                    )
                )
            )

            strength_component = (
                min(
                    100,
                    max(
                        0,
                        strength
                    )
                )
            )


            # -----------------------------------------
            # Candidate score
            # -----------------------------------------

            candidate_score = (
                trend_component * 0.40
                +
                momentum_component * 0.30
                +
                strength_component * 0.30
            )


            candidate_score = round(
                candidate_score,
                2
            )


            # -----------------------------------------
            # Classification
            # -----------------------------------------

            if (
                candidate_score >= 80
                and score >= 80
            ):

                status = "READY"


            elif (
                candidate_score >= 65
                and score >= 65
            ):

                status = "EARLY"


            else:

                status = "IGNORE"


            result = {

                "symbol": item.get(
                    "symbol"
                ),

                "score": round(
                    score,
                    2
                ),

                "regime": regime,

                "trend_component": round(
                    trend_component,
                    2
                ),

                "momentum_component": round(
                    momentum_component,
                    2
                ),

                "strength_component": round(
                    strength_component,
                    2
                ),

                "candidate_score": candidate_score,

                "status": status
            }


            return result


        except Exception as error:

            return {

                "symbol": item.get(
                    "symbol"
                ) if item else None,

                "score": 0,

                "candidate_score": 0,

                "status": "IGNORE",

                "error": str(error)
            }


    def detect(self, results):

        self.results = []


        if results is None:

            return []


        for item in results:

            result = self.analyze(
                item
            )

            self.results.append(
                result
            )


        self.results.sort(
            key=lambda item: item.get(
                "candidate_score",
                0
            ),
            reverse=True
        )


        for index, item in enumerate(
            self.results,
            start=1
        ):

            item[
                "candidate_rank"
            ] = index


        return self.results