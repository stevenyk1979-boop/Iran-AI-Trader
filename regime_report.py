"""
Iran AI Trader Professional
Market Regime Report
Sprint30-B
"""


class RegimeReport:


    def __init__(self):

        pass


    # -----------------------------------

    def risk_level(self, regime):

        if regime == "BULL":

            return "LOW"

        elif regime == "SIDEWAYS":

            return "MEDIUM"

        elif regime == "BEAR":

            return "HIGH"

        else:

            return "UNKNOWN"



    # -----------------------------------

    def trading_mode(self, regime):

        if regime == "BULL":

            return [

                "Buying Allowed",

                "Normal Position Size"

            ]


        elif regime == "SIDEWAYS":

            return [

                "Selective Buying",

                "Reduced Position Size"

            ]


        elif regime == "BEAR":

            return [

                "Buying Restricted",

                "Capital Protection Mode"

            ]


        else:

            return [

                "Waiting For Data"

            ]



    # -----------------------------------

    def recommendation(self, regime):

        if regime == "BULL":

            return (

                "Focus on high score candidates"

            )


        elif regime == "SIDEWAYS":

            return (

                "Wait for stronger confirmation"

            )


        elif regime == "BEAR":

            return (

                "Avoid aggressive entries"

            )


        return (

            "No recommendation"

        )



    # -----------------------------------

    def show(self, regime):


        print()

        print("=" * 60)

        print(

            "IRAN AI TRADER MARKET REGIME REPORT"

        )

        print("=" * 60)


        print()

        print(

            "Market Condition :",

            regime["regime"]

        )


        print(

            "Market Score     :",

            regime["score"]

        )


        print(

            "Confidence       :",

            str(regime["confidence"]) + "%"

        )


        print()

        print(

            "Risk Level       :",

            self.risk_level(

                regime["regime"]

            )

        )


        print()

        print(

            "Trading Mode"

        )

        print("-" * 40)



        for item in self.trading_mode(

            regime["regime"]

        ):

            print(

                "✓",

                item

            )



        print()

        print(

            "Recommendation"

        )

        print("-" * 40)


        print(

            self.recommendation(

                regime["regime"]

            )

        )