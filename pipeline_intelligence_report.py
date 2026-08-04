"""
Iran AI Trader Professional
Pipeline Intelligence Report
Sprint35
"""


class PipelineIntelligenceReport:


    def __init__(self):

        pass



    # -------------------------------------

    def show(

        self,

        results

    ):

        """
        Display pipeline intelligence report
        """


        print()

        print("=" * 70)

        print(

            "PIPELINE INTELLIGENCE REPORT"

        )

        print("=" * 70)



        print()


        print(

            "Total Analyzed:",

            len(results)

        )



        approved = [

            item

            for item in results

            if item.get(

                "decision"

            )

            ==

            "APPROVED BUY"

        ]



        print(

            "Approved Trades:",

            len(approved)

        )



        print()

        print(

            "TOP AI OPPORTUNITIES"

        )

        print("-" * 70)



        for index, item in enumerate(

            results[:10],

            start=1

        ):


            print()


            print(

                index,

                ")",

                item.get(

                    "symbol",

                    "-"

                )

            )


            print(

                "Final AI Score:",

                item.get(

                    "final_ai_score",

                    0

                )

            )


            print(

                "Decision:",

                item.get(

                    "decision",

                    "UNKNOWN"

                )

            )


            print(

                "-" * 40

            )



        print()

        print("=" * 70)