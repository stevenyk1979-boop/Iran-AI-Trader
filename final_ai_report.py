"""
Iran AI Trader Professional
Final AI Report Engine
Sprint32-H
"""


class FinalAIReport:


    def __init__(self):

        pass



    # -------------------------------------

    def show(

        self,

        result

    ):


        regime = result.get(

            "regime",

            {}

        )


        decisions = result.get(

            "decisions",

            []

        )


        approved = []


        for item in decisions:


            capital = item.get(

                "capital",

                {}

            )


            if capital.get(

                "allowed",

                False

            ):

                approved.append(item)



        approved.sort(

            key=lambda x: x.get(

                "score",

                0

            ),

            reverse=True

        )



        print()

        print("=" * 70)

        print(

            "IRAN AI TRADER FINAL REPORT"

        )

        print("=" * 70)



        print()

        print(

            "Market Regime :",

            regime.get(

                "regime"

            )

        )


        print(

            "Market Score  :",

            regime.get(

                "score"

            )

        )


        print(

            "Confidence    :",

            regime.get(

                "confidence"

            ),

            "%"

        )



        print()

        print(

            "Candidates    :",

            len(

                result.get(

                    "candidates",

                    []

                )

            )

        )


        print(

            "Approved      :",

            len(approved)

        )



        print()

        print(

            "TOP CAPITAL OPPORTUNITIES"

        )

        print("-" * 70)



        for index, item in enumerate(

            approved[:10],

            1

        ):


            capital = item.get(

                "capital",

                {}

            )


            print()

            print(

                f"{index}) {item.get('symbol')}"

            )


            print(

                "AI Score :", 

                item.get(

                    "score"

                )

            )


            print(

                "Signal   :",

                item.get(

                    "signal"

                )

            )


            print(

                "Capital  :",

                capital.get(

                    "capital",

                    0

                )

            )


            print(

                "Shares   :",

                capital.get(

                    "shares",

                    0

                )

            )


            print("-" * 40)