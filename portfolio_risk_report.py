"""
Iran AI Trader Professional
Portfolio Risk Report
Sprint33-D
"""


class PortfolioRiskReport:


    def __init__(self):

        pass



    # -------------------------------------

    def show(

        self,

        result

    ):

        """
        Display portfolio risk report
        """


        print()

        print("=" * 70)

        print(

            "PORTFOLIO RISK REPORT"

        )

        print("=" * 70)



        print()


        print(

            "Drawdown :",

            result.get(

                "drawdown",

                0

            ),

            "%"

        )



        print(

            "Volatility:",

            result.get(

                "volatility",

                0

            ),

            "%"

        )



        print(

            "Risk Score:",

            result.get(

                "risk_score",

                0

            )

        )



        print(

            "Risk Level:",

            result.get(

                "risk_level",

                "UNKNOWN"

            )

        )



        print()

        print(

            "Recommended Action"

        )

        print("-" * 70)



        print(

            result.get(

                "action",

                "NORMAL"

            )

        )



        print()

        print("=" * 70)