"""
Iran AI Trader Professional
Decision Engine
"""

from decision_result import DecisionResult
from confidence_engine import ConfidenceEngine


class DecisionEngine:


    def __init__(self):

        self.confidence = ConfidenceEngine()



    # ---------------------------------

    def decide(

        self,

        symbol,

        engines,

        risk

    ):


        total_score = 0

        total_max = 0

        reasons = []



        # ---------------------------------
        # Collect Engine Scores
        # ---------------------------------

        for name, result in engines.items():


            total_score += result.get(

                "score",

                0

            )


            total_max += result.get(

                "max_score",

                0

            )


            reasons.extend(

                result.get(

                    "reason",

                    []

                )

            )



        # ---------------------------------
        # Normalize Score
        # ---------------------------------

        if total_max == 0:

            raw_score = 0

        else:

            raw_score = (

                total_score /

                total_max

            ) * 100



        # ---------------------------------
        # Confidence
        # ---------------------------------

        confidence_result = self.confidence.calculate(

            engines

        )


        confidence = confidence_result["confidence"]



        # ---------------------------------
        # Risk Adjustment
        # ---------------------------------

        risk_value = risk.get(

            "risk",

            100

        )


        final_score = raw_score * (

            1 - risk_value / 200

        )


        final_score = round(

            max(

                0,

                final_score

            ),

            2

        )



        # ---------------------------------
        # Decision
        # ---------------------------------

        if final_score >= 85 and confidence >= 75:

            signal = "STRONG BUY"


        elif final_score >= 70 and confidence >= 60:

            signal = "BUY"


        elif final_score >= 50:

            signal = "HOLD"


        else:

            signal = "SELL"



        # ---------------------------------
        # Result
        # ---------------------------------

        return DecisionResult(

            symbol=symbol,

            score=final_score,

            confidence=confidence,

            risk=risk_value,

            signal=signal,

            reasons=reasons,

            detail={

                "raw_score": round(

                    raw_score,

                    2

                ),

                "final_score": final_score,

                "engines": engines,

                "risk": risk,

                "confidence": confidence_result

            }

        )