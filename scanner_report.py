"""
Iran AI Trader Professional
Scanner Report
"""

from market_statistics import MarketStatistics
from ai_explanation import AIExplanation

class ScannerReport:

    def __init__(self):

        self.statistics = MarketStatistics()


    # ---------------------------------

    def show(self, ranking):

        print()

        print("=" * 70)

        print("Scanner Report")

        print("=" * 70)


        print(

            f"{'Symbol':<12}"

            f"{'Score':>10}"

            f"{'Confidence':>12}"

            f"{'Risk':>8}"

            f"{'Signal':>18}"

        )


        print("-" * 70)



        for row in ranking:


            print(

                f"{row['symbol']:<12}"

                f"{row['score']:>10.2f}"

                f"{row.get('confidence', 0):>12.2f}"

                f"{row.get('risk', 0):>8}"

                f"{row['signal']:>18}"

            )



        if not ranking:

            print()

            print("No symbols found.")

            return



        best = self.statistics.best(ranking)

        worst = self.statistics.worst(ranking)

        avg = self.statistics.average_score(ranking)



        print()

        print("=" * 70)

        print("Market Statistics")

        print("=" * 70)


        print(

            "Best Symbol   :",

            best["symbol"]

        )


        print(

            "Best Score    :",

            best["score"]

        )


        print(

            "Worst Symbol  :",

            worst["symbol"]

        )


        print(

            "Worst Score   :",

            worst["score"]

        )


        print(

            "Average Score :",

            avg

        )