"""
Iran AI Trader Professional
Trade Decision Engine
Sprint28-E
"""


class TradeDecisionEngine:


    def decide(self, candidate):

        category = candidate.get(

            "category",

            "REJECT"

        )


        score = candidate.get(

            "score",

            0

        )


        confidence = candidate.get(

            "confidence",

            0

        )


        risk = candidate.get(

            "risk",

            100

        )


        reasons = []



        if category == "READY":

            decision = "BUY"

            reasons.append(

                "Entry validation passed"

            )


        elif category == "WATCH":

            decision = "WAIT"

            reasons.append(

                "Waiting for entry confirmation"

            )


        else:

            decision = "IGNORE"

            reasons.append(

                "Candidate rejected"

            )



        if score >= 85:

            reasons.append(

                "Strong AI score"

            )


        if confidence >= 80:

            reasons.append(

                "High confidence"

            )


        if risk <= 20:

            reasons.append(

                "Controlled risk"

            )



        return {


            "symbol": candidate.get(

                "symbol"

            ),


            "decision": decision,


            "score": score,


            "confidence": confidence,


            "risk": risk,


            "reasons": reasons

        }