"""
Iran AI Trader Professional
Sector Report
Sprint33-B
"""


class SectorReport:


    def __init__(self):

        pass



    # -------------------------------------

    def show(

        self,

        result

    ):

        """
        Display sector allocation report
        """

        distribution = result.get(

            "distribution",

            {}

        )


        warnings = result.get(

            "warnings",

            []

        )


        status = result.get(

            "status",

            "UNKNOWN"

        )



        print()

        print("=" * 70)

        print(

            "SECTOR ALLOCATION REPORT"

        )

        print("=" * 70)



        print()


        print(

            "Sector Distribution"

        )

        print("-" * 70)



        for sector, percent in distribution.items():


            print(

                f"{sector:<15}: {percent}%"

            )



        print()

        print(

            "Risk Check"

        )

        print("-" * 70)



        if warnings:


            for warning in warnings:

                print(

                    "WARNING:",

                    warning

                )


        else:

            print(

                "Status :", 

                status

            )



        print()

        print("=" * 70)