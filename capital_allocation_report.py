"""
Iran AI Trader Professional
Capital Allocation Report Engine
Sprint32-G
"""


class CapitalAllocationReport:


    def __init__(self):

        pass



    # -------------------------------------

    def approved_only(

        self,

        decisions

    ):

        return [

            item

            for item in decisions

            if item.get(

                "capital",

                {}

            ).get(

                "allowed",

                False

            )

        ]



    # -------------------------------------

    def sort_by_score(

        self,

        decisions

    ):

        return sorted(

            decisions,

            key=lambda x: x.get(

                "score",

                0

            ),

            reverse=True

        )



    # -------------------------------------

    def show(

        self,

        decisions,

        limit=10

    ):


        approved = self.approved_only(

            decisions

        )


        ranked = self.sort_by_score(

            approved

        )


        print()

        print("=" * 70)

        print(

            "CAPITAL ALLOCATION REPORT"

        )

        print("=" * 70)



        print()

        print(

            "Approved Trades:",

            len(approved)

        )


        print()

        print(

            "TOP CAPITAL OPPORTUNITIES"

        )

        print("-" * 70)



        for item in ranked[:limit]:


            capital = item.get(

                "capital",

                {}

            )


            print()


            print(

                "Symbol :", 

                item.get(

                    "symbol"

                )

            )


            print(

                "Score  :",

                item.get(

                    "score"

                )

            )


            print(

                "Signal :",

                item.get(

                    "signal"

                )

            )


            print(

                "Capital:",

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

                "Status :",

                "APPROVED"

            )


            print("-" * 40)