"""
Iran AI Trader V2.0 Alpha
Scanner Report
"""

from market_statistics import MarketStatistics


class ScannerReport:

    def __init__(self):

        self.statistics = MarketStatistics()

    def show(self, ranking):

        print()
        print("=" * 60)
        print("Scanner Report")
        print("=" * 60)

        print(
            f"{'Symbol':<12}"
            f"{'Score':>8}"
            f"{'Signal':>18}"
        )

        print("-" * 42)

        for row in ranking:

            print(
                f"{row['symbol']:<12}"
                f"{row['score']:>8}"
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
        print("=" * 60)
        print("Market Statistics")
        print("=" * 60)

        print("Best Symbol   :", best["symbol"])
        print("Best Score    :", best["score"])

        print("Worst Symbol  :", worst["symbol"])
        print("Worst Score   :", worst["score"])

        print("Average Score :", avg)