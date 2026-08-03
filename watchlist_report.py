"""
Iran AI Trader Professional
Watch List Report
Sprint28-B
"""

from watchlist import WatchList


class WatchListReport:


    def __init__(self):

        self.watchlist = WatchList()



    # -------------------------------------

    def category(self, score):

        if score >= 85:

            return "STRONG CANDIDATE"


        elif score >= 75:

            return "CANDIDATE"


        elif score >= 65:

            return "MONITOR"


        else:

            return "LOW"



    # -------------------------------------

    def print_section(

        self,

        title,

        items

    ):


        print()

        print("=" * 70)

        print(title)

        print("=" * 70)



        if not items:

            print(

                "No symbols"

            )

            return



        for item in items:


            print(

                f"{item['symbol']:<12}"

                f" Score: {item['score']:<8}"

                f" Signal: {item['signal']}"

            )



    # -------------------------------------

    def show(self):


        items = self.watchlist.all()


        strong = []

        candidate = []

        monitor = []



        for item in items:


            level = self.category(

                item["score"]

            )


            if level == "STRONG CANDIDATE":

                strong.append(item)


            elif level == "CANDIDATE":

                candidate.append(item)


            elif level == "MONITOR":

                monitor.append(item)



        print()

        print("=" * 70)

        print(

            "AI WATCH LIST REPORT"

        )

        print("=" * 70)


        print(

            "Total Watch List:",

            len(items)

        )



        self.print_section(

            "🔥 STRONG CANDIDATES",

            strong

        )


        self.print_section(

            "⭐ CANDIDATES",

            candidate

        )


        self.print_section(

            "👀 MONITOR",

            monitor

        )



        print()

        print(

            "Top 10 Opportunities"

        )

        print("-" * 70)



        for item in items[:10]:

            print(

                item["symbol"],

                "=>",

                item["score"]

            )



# -----------------------------------------

# Run directly for testing

if __name__ == "__main__":


    report = WatchListReport()

    report.show()