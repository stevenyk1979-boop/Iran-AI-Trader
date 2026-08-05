"""
Iran AI Trader Professional

Scanner Health Report
Sprint43.6
"""


from collections import Counter


class ScannerHealthReport:

    def __init__(self):

        self.errors = []

    # ----------------------------------

    def add(self, symbol, error):

        self.errors.append({

            "symbol": symbol,

            "error": str(error)

        })

    # ----------------------------------

    def summary(self):

        counter = Counter()

        for item in self.errors:

            counter[item["error"]] += 1

        return counter

    # ----------------------------------

    def print_report(self):

        print()

        print("=" * 70)
        print("SCANNER HEALTH REPORT")
        print("=" * 70)

        if not self.errors:

            print("No Scanner Errors")

            return

        counter = self.summary()

        print()

        for err, count in counter.items():

            print(f"{count:5d}   {err}")

        print()

        print("-" * 70)

        print("Sample Errors")

        print("-" * 70)

        for item in self.errors[:20]:

            print(

                item["symbol"],

                "->",

                item["error"]

            )