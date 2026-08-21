# `test_top10_scanner_v2.py`


"""
Iran AI Trader Professional

Scanner V2

Top 10 Ranking Validation
"""

from scanner_v2.scanner import Scanner


# ============================================================
# Fake History
# ============================================================

class FakeHistory:

    def __init__(self, symbol):

        self.symbol = symbol

    def close_prices(self):

        try:

            number = int(
                self.symbol.replace(
                    "TEST",
                    ""
                )
            )

        except ValueError:

            number = 1

        offset = number * 0.5

        return [

            100
            + offset
            + i

            for i in range(30)

        ]


# ============================================================
# Fake Market Service
# ============================================================

class FakeMarketService:

    def history(self, symbol):

        return FakeHistory(symbol)

    def get_history(self, symbol):

        return FakeHistory(symbol)


# ============================================================
# Fake Market Loader
# ============================================================

class FakeMarketLoader:

    def load_symbols(self):

        return [

            "TEST1",
            "TEST2",
            "TEST3",
            "TEST4",
            "TEST5",
            "TEST6",
            "TEST7",
            "TEST8",
            "TEST9",
            "TEST10",
            "TEST11",
            "TEST12"

        ]


# ============================================================
# Create Scanner
# ============================================================

def create_scanner():

    scanner = Scanner()

    scanner.market_loader = (
        FakeMarketLoader()
    )

    scanner.history_loader.market_service = (
        FakeMarketService()
    )

    return scanner


# ============================================================
# Print Results
# ============================================================

def print_results(
    title,
    results
):

    print()

    print("=" * 60)

    print(title)

    print("=" * 60)

    print()

    for index, item in enumerate(
        results,
        start=1
    ):

        print(
            f"{index:02d}. "
            f"{item['symbol']} "
            f"| SCORE: {item['score']} "
            f"| {item['decision']}"
        )


# ============================================================
# Validation
# ============================================================

def run_validation():

    print()

    print("=" * 60)

    print(
        "TOP 10 RANKING VALIDATION"
    )

    print("=" * 60)

    print()

    scanner = create_scanner()

    results = scanner.scan()

    # --------------------------------------------------------
    # Validate all 12 symbols
    # --------------------------------------------------------

    if len(results) != 12:

        raise Exception(
            f"Expected 12 results, "
            f"got {len(results)}"
        )

    print(
        f"TOTAL VALID RESULTS: "
        f"{len(results)}"
    )

    # --------------------------------------------------------
    # Validate result structures
    # --------------------------------------------------------

    for item in results:

        if "symbol" not in item:

            raise Exception(
                "Result symbol is missing"
            )

        if "score" not in item:

            raise Exception(
                f"Score missing for "
                f"{item['symbol']}"
            )

        if "ranking_breakdown" not in item:

            raise Exception(
                f"Ranking breakdown missing "
                f"for {item['symbol']}"
            )

        if item["decision"] == "FAILED":

            raise Exception(
                f"Unexpected FAILED result: "
                f"{item}"
            )

    print(
        "ALL RESULT STRUCTURES: PASS"
    )

    # --------------------------------------------------------
    # Validate ranking breakdown
    # --------------------------------------------------------

    for item in results:

        breakdown = (
            item["ranking_breakdown"]
        )

        if "price" not in breakdown:

            raise Exception(
                f"Price breakdown missing: "
                f"{item['symbol']}"
            )

        if "trend" not in breakdown:

            raise Exception(
                f"Trend breakdown missing: "
                f"{item['symbol']}"
            )

        if "momentum" not in breakdown:

            raise Exception(
                f"Momentum breakdown missing: "
                f"{item['symbol']}"
            )

        weight_sum = sum(

            component["weight"]

            for name, component
            in breakdown.items()

            if name != "final_score"

        )

        if round(
            weight_sum,
            2
        ) != 1.0:

            raise Exception(
                f"Invalid weight sum for "
                f"{item['symbol']}: "
                f"{weight_sum}"
            )

    print(
        "RANKING BREAKDOWN: PASS"
    )

    # --------------------------------------------------------
    # Sort by score
    # --------------------------------------------------------

    ranked_results = sorted(

        results,

        key=lambda item:
            item["score"],

        reverse=True

    )

    # --------------------------------------------------------
    # Select Top 10
    # --------------------------------------------------------

    top10 = ranked_results[:10]

    if len(top10) != 10:

        raise Exception(
            f"Expected Top 10, "
            f"got {len(top10)}"
        )

    print(
        "TOP 10 COUNT: PASS"
    )

    # --------------------------------------------------------
    # Validate uniqueness
    # --------------------------------------------------------

    symbols = [

        item["symbol"]

        for item in top10

    ]

    if len(symbols) != len(
        set(symbols)
    ):

        raise Exception(
            "Duplicate symbol found "
            "in Top 10"
        )

    print(
        "TOP 10 UNIQUENESS: PASS"
    )

    # --------------------------------------------------------
    # Validate descending order
    # --------------------------------------------------------

    for i in range(
        len(top10) - 1
    ):

        current_score = (
            top10[i]["score"]
        )

        next_score = (
            top10[i + 1]["score"]
        )

        if current_score < next_score:

            raise Exception(
                "Top 10 ranking order "
                "is not descending"
            )

    print(
        "TOP 10 ORDER: PASS"
    )

    # --------------------------------------------------------
    # Print Top 10
    # --------------------------------------------------------

    print_results(

        "SCANNER V2 TOP 10",

        top10

    )

    print()

    print("=" * 60)

    print(
        "TOP 10 VALIDATION: PASS"
    )

    print("=" * 60)

    print()

    print(
        "VALIDATION FINISHED"
    )


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":

    run_validation()

