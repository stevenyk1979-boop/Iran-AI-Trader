"""
Iran AI Trader Professional

Scanner V2

Sprint45-03

Regime-Aware Decision Engine

Adjusts final trading decisions according to
the current market regime.
"""


class RegimeAwareDecision:

    # -------------------------------------------------
    # Decision thresholds by market regime
    # -------------------------------------------------

    REGIME_THRESHOLDS = {

        "STRONG BULL": {
            "strong_watch": 80,
            "watch": 65,
        },

        "BULL": {
            "strong_watch": 80,
            "watch": 65,
        },

        "EARLY BULL": {
            "strong_watch": 82,
            "watch": 68,
        },

        "SIDEWAYS": {
            "strong_watch": 85,
            "watch": 72,
        },

        "BEAR": {
            "strong_watch": 90,
            "watch": 78,
        },

        "STRONG BEAR": {
            "strong_watch": 95,
            "watch": 85,
        },

        "UNKNOWN": {
            "strong_watch": 85,
            "watch": 70,
        },
    }


    # -------------------------------------------------
    # Constructor
    # -------------------------------------------------

    def __init__(self):

        self.results = []


    # -------------------------------------------------
    # Get thresholds
    # -------------------------------------------------

    def get_thresholds(self, regime):

        return self.REGIME_THRESHOLDS.get(
            regime,
            self.REGIME_THRESHOLDS["UNKNOWN"]
        )


    # -------------------------------------------------
    # Decide
    # -------------------------------------------------

    def decide(
        self,
        score,
        regime
    ):

        try:

            score = float(score)

            thresholds = self.get_thresholds(
                regime
            )

            strong_watch_threshold = (
                thresholds["strong_watch"]
            )

            watch_threshold = (
                thresholds["watch"]
            )


            if score >= strong_watch_threshold:

                decision = "STRONG WATCH"

            elif score >= watch_threshold:

                decision = "WATCH"

            else:

                decision = "IGNORE"


            result = {

                "score": round(
                    score,
                    2
                ),

                "regime": regime,

                "strong_watch_threshold": (
                    strong_watch_threshold
                ),

                "watch_threshold": (
                    watch_threshold
                ),

                "decision": decision
            }


            self.results.append(
                result
            )


            return result


        except Exception as error:

            return {

                "score": 0,

                "regime": regime,

                "strong_watch_threshold": 85,

                "watch_threshold": 70,

                "decision": "IGNORE",

                "error": str(error)
            }