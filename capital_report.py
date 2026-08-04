"""
Iran AI Trader Professional
Capital Report Engine
Sprint32-F
"""


class CapitalReport:


    def __init__(self):

        pass



    # -------------------------------------

    def status_text(

        self,

        capital

    ):

        if capital.get(

            "allowed",

            False

        ):

            return "APPROVED"

        else:

            return "BLOCKED"



    # -------------------------------------

    def show(

        self,

        decision

    ):

        """
        Display capital allocation report
        """

        capital = decision.get(

            "capital",

            {}

        )


        print()

        print("=" * 60)

        print(

            "CAPITAL ALLOCATION REPORT"

        )

        print("=" * 60)



        print()

        print(

            "Symbol :",

            decision.get(

                "symbol"

            )

        )


        print(

            "Decision :",

            decision.get(

                "signal"

            )

        )


        print(

            "AI Score :",

            decision.get(

                "score",

                0

            )

        )


        print()

        print(

            "Allocation :",


            capital.get(

                "allocation_percent",

                0

            ),

            "%"

        )


        print(

            "Capital :",

            capital.get(

                "capital",

                0

            )

        )


        print(

            "Shares :",

            capital.get(

                "shares",

                0

            )

        )


        print(

            "Capital Used :",

            capital.get(

                "capital_used",

                0

            )

        )


        print()

        print(

            "Status :",

            self.status_text(

                capital

            )

        )


        print()

        print("=" * 60)