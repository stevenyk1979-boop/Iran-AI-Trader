"""
Iran AI Trader Professional
AI Decision Report
Sprint28-F
"""


class AIDecisionReport:


    def generate(self, decisions):

        report = {


            "BUY": [],

            "WAIT": [],

            "IGNORE": []

        }


        for item in decisions:


            decision = item.get(

                "decision",

                "IGNORE"

            )


            if decision not in report:

                decision = "IGNORE"


            report[decision].append(

                item

            )


        return report



    # ---------------------------------


    def print_report(self, report):


        print()

        print("=" * 60)

        print("AI TRADE DECISION REPORT")

        print("=" * 60)



        sections = [

            ("BUY", "🔥 BUY"),

            ("WAIT", "⏳ WAIT"),

            ("IGNORE", "❌ IGNORE")

        ]



        for key, title in sections:


            print()

            print(title)

            print("-" * 60)



            if not report[key]:

                print("None")

                continue



            for item in report[key]:


                print(

                    item.get(

                        "symbol",

                        ""

                    )

                )


                print(

                    "Score:",

                    item.get(

                        "score",

                        0

                    )

                )


                print(

                    "Confidence:",

                    item.get(

                        "confidence",

                        0

                    )

                )


                print(

                    "Risk:",

                    item.get(

                        "risk",

                        0

                    )

                )


                print(

                    "Reasons:"

                )


                for reason in item.get(

                    "reasons",

                    []

                ):

                    print(

                        "✓",

                        reason

                    )


                print()