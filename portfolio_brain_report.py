"""
Iran AI Trader Professional
Portfolio Brain Report
Sprint34
"""


class PortfolioBrainReport:


    def __init__(self):

        pass



    # -------------------------------------

    def show(

        self,

        result

    ):

        """
        Display AI Portfolio Brain Report
        """


        print()

        print("=" * 70)

        print(

            "AI PORTFOLIO BRAIN REPORT"

        )

        print("=" * 70)



        print()


        print(

            "Symbol:",

            result.get(

                "symbol",

                "-"

            )

        )



        print("-" * 70)



        print(

            "Technical Score:",

            result.get(

                "technical_score",

                0

            )

        )



        print(

            "Smart Money Score:",

            result.get(

                "smart_money_score",

                0

            )

        )



        print(

            "Portfolio Score:",

            result.get(

                "portfolio_score",

                0

            )

        )



        print(

            "Risk Score:",

            result.get(

                "risk_score",

                0

            )

        )



        print()

        print(

            "Final AI Score:",

            result.get(

                "final_ai_score",

                0

            )

        )



        print()

        print(

            "Decision:",

            result.get(

                "decision",

                "UNKNOWN"

            )

        )



        print()

        print("=" * 70)