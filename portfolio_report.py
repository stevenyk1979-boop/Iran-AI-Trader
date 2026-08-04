"""
Iran AI Trader Professional
Portfolio Report
Sprint33-A
"""


class PortfolioReport:


    def show(

        self,

        result

    ):


        print()

        print("=" * 70)

        print(

            "PORTFOLIO OPTIMIZER REPORT"

        )

        print("=" * 70)



        print()

        print(

            "Total Candidates:",

            result.get(

                "total_candidates"

            )

        )


        print(

            "Quality Candidates:",

            result.get(

                "quality_candidates"

            )

        )



        print()

        print(

            "SELECTED PORTFOLIO"

        )

        print("-" * 70)



        for item in result.get(

            "selected",

            []

        ):


            print()

            print(

                "Symbol:",

                item.get(

                    "symbol"

                )

            )


            print(

                "Score:",

                item.get(

                    "score"

                )

            )


            print(

                "Signal:",

                item.get(

                    "signal"

                )

            )

            print("-" * 40)