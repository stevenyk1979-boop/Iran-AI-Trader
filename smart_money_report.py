"""
Iran AI Trader Professional
Smart Money Report
Sprint31-A
"""


class SmartMoneyReport:


    def show(self, result):


        print()

        print("=" * 60)

        print("SMART MONEY REPORT")

        print("=" * 60)



        print()

        print(

            "Symbol :", 

            result["symbol"]

        )


        print(

            "Score  :", 

            result["score"]

        )


        print(

            "Status :", 

            result["status"]

        )



        print()

        print("Signals")

        print("-" * 40)



        if result["signals"]:


            for signal in result["signals"]:

                print(

                    "✓",

                    signal

                )

        else:

            print(

                "No signal"

            )