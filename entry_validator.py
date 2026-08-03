"""
Iran AI Trader Professional
Entry Validator
Sprint28-C
"""


class EntryValidator:


    def validate(self, result):

        score = result.get(
            "score",
            0
        )

        confidence = result.get(
            "confidence",
            0
        )

        risk = result.get(
            "risk",
            100
        )

        signal = result.get(
            "signal",
            "HOLD"
        )


        checks = {

            "score": score >= 75,

            "confidence": confidence >= 60,

            "risk": risk <= 25,

            "signal": signal in [

                "BUY",

                "STRONG BUY"

            ]

        }


        passed = sum(

            1

            for value in checks.values()

            if value

        )


        if passed == 4:

            status = "READY TO BUY"


        elif passed >= 2:

            status = "WATCH"


        else:

            status = "WAIT"



        return {

            "status": status,

            "checks": checks,

            "passed": passed,

            "total": len(checks)

        }