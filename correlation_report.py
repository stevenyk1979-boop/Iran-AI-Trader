"""
Iran AI Trader Professional
Correlation Report
Sprint33-C
"""


from correlation_config import (
    MAX_PAIRS_REPORT
)



class CorrelationReport:


    def __init__(self):

        pass



    # -------------------------------------

    def show(

        self,

        result

    ):

        """

        Display correlation analysis report

        """


        print()

        print("=" * 70)

        print(

            "CORRELATION REPORT"

        )

        print("=" * 70)



        print()


        print(

            "Pairs Checked:",

            result.get(

                "pairs_checked",

                0

            )

        )



        print()

        print(

            "Correlation Pairs"

        )

        print("-" * 70)



        pairs = result.get(

            "pairs",

            []

        )



        for item in pairs[:MAX_PAIRS_REPORT]:


            print()


            print(

                "Pair:",

                item.get(

                    "symbol_a"

                ),

                "-",

                item.get(

                    "symbol_b"

                )

            )


            print(

                "Correlation:",

                item.get(

                    "correlation"

                )

            )


            print(

                "Status:",

                item.get(

                    "status"

                )

            )


            print(

                "-" * 40

            )



        print()


        print(

            "Risk Warnings"

        )

        print("-" * 70)



        warnings = result.get(

            "warnings",

            []

        )



        if warnings:


            for warning in warnings:


                print(

                    "WARNING:",

                    warning.get(

                        "symbol_a"

                    ),

                    "-",

                    warning.get(

                        "symbol_b"

                    ),

                    "High correlation"

                )



        else:


            print(

                "No correlation risk detected"

            )



        print()

        print("=" * 70)