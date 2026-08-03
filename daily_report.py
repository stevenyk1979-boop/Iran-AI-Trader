"""
Iran AI Trader Professional
Daily AI Market Report
Sprint29-A
"""


from datetime import datetime



class DailyReport:


    def generate(

        self,

        decisions,

        total_symbols=0,

        watchlist_size=0

    ):


        report = {


            "date":

                datetime.now().strftime(
                    "%Y-%m-%d"
                ),


            "total_symbols":

                total_symbols,


            "watchlist_size":

                watchlist_size,


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


    def print_report(

        self,

        report

    ):


        print()

        print("=" * 60)

        print("IRAN AI TRADER DAILY REPORT")

        print("=" * 60)


        print()

        print(

            "Date:",

            report["date"]

        )


        print(

            "Symbols scanned:",

            report["total_symbols"]

        )


        print(

            "WatchList:",

            report["watchlist_size"]

        )



        sections = [

            ("BUY", "🔥 BUY SIGNALS"),

            ("WAIT", "⏳ WAIT LIST"),

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

                    ),

                    "| Score:",

                    item.get(

                        "score",

                        0

                    ),

                    "| Decision:",

                    item.get(

                        "decision",

                        ""

                    )

                )


        print()

        print("=" * 60)