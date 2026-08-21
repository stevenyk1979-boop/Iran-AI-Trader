"""
Iran AI Trader Professional

Scanner V2

Sprint44-35

Scanner V2 Integration Test
"""

from scanner_v2.scanner import Scanner
from scanner_v2.config import ScannerConfig


class FakeHistory:

    def close_prices(self):

        return [
            100 + i
            for i in range(30)
        ]


class FakeMarketService:

    def history(self, symbol):

        return FakeHistory()


class FakeMarketLoader:

    def load_symbols(self):

        return [
            "TEST1",
            "TEST2"
        ]


def create_scanner(config=None):

    scanner = Scanner()

    if config is not None:

        scanner.config = config

        if hasattr(
            scanner,
            "ranking_engine"
        ):

            scanner.ranking_engine.config = config

        if hasattr(
            scanner,
            "history_loader"
        ):

            scanner.history_loader.config = config

    scanner.market_loader = FakeMarketLoader()

    scanner.history_loader.market_service = (
        FakeMarketService()
    )

    return scanner


def print_results(
    title,
    results
):

    print()

    print("=" * 60)

    print(title)

    print("=" * 60)

    print()

    for item in results:

        print(item)


def validate_default_results(
    results
):

    if len(results) != 2:

        raise Exception(
            "Expected 2 default results"
        )

    for item in results:

        # -------------------------------------------------
        # Final score
        # -------------------------------------------------

        if item["score"] != 83.22:

            raise Exception(
                f"Default score regression: "
                f"{item['score']}"
            )

        # -------------------------------------------------
        # Decision
        # -------------------------------------------------

        if item["decision"] != "STRONG WATCH":

            raise Exception(
                f"Unexpected decision: "
                f"{item['decision']}"
            )

        # -------------------------------------------------
        # Ranking breakdown
        # -------------------------------------------------

        breakdown = item.get(
            "ranking_breakdown"
        )

        if breakdown is None:

            raise Exception(
                "ranking_breakdown is missing"
            )

        # -------------------------------------------------
        # Price
        # -------------------------------------------------

        if breakdown["price"]["score"] != 69.0:

            raise Exception(
                "Invalid price score"
            )

        if breakdown["price"]["weight"] != 0.5:

            raise Exception(
                "Invalid default price weight"
            )

        if breakdown["price"]["contribution"] != 34.5:

            raise Exception(
                "Invalid price contribution"
            )

        # -------------------------------------------------
        # Trend
        # -------------------------------------------------

        if breakdown["trend"]["score"] != 97.4:

            raise Exception(
                "Invalid trend score"
            )

        if breakdown["trend"]["weight"] != 0.3:

            raise Exception(
                "Invalid default trend weight"
            )

        if breakdown["trend"]["contribution"] != 29.22:

            raise Exception(
                "Invalid trend contribution"
            )

        # -------------------------------------------------
        # Momentum
        # -------------------------------------------------

        if breakdown["momentum"]["score"] != 97.5:

            raise Exception(
                "Invalid momentum score"
            )

        if breakdown["momentum"]["weight"] != 0.2:

            raise Exception(
                "Invalid default momentum weight"
            )

        if breakdown["momentum"]["contribution"] != 19.5:

            raise Exception(
                "Invalid momentum contribution"
            )

        # -------------------------------------------------
        # Final breakdown score
        # -------------------------------------------------

        if breakdown["final_score"] != 83.22:

            raise Exception(
                "Invalid breakdown final score"
            )


def validate_changed_weight_results(
    results
):

    if len(results) != 2:

        raise Exception(
            "Expected 2 changed-weight results"
        )

    for item in results:

        # -------------------------------------------------
        # Expected score
        #
        # Price    = 69.0 * 0.4 = 27.60
        # Trend    = 97.4 * 0.4 = 38.96
        # Momentum = 97.5 * 0.2 = 19.50
        #
        # Total = 86.06
        # -------------------------------------------------

        if item["score"] != 86.06:

            raise Exception(
                f"Changed-weight score failed: "
                f"{item['score']}"
            )

        breakdown = item.get(
            "ranking_breakdown"
        )

        if breakdown is None:

            raise Exception(
                "Changed-weight breakdown missing"
            )

        # -------------------------------------------------
        # Price weight
        # -------------------------------------------------

        if breakdown["price"]["weight"] != 0.4:

            raise Exception(
                "Price weight was not changed"
            )

        if breakdown["price"]["contribution"] != 27.6:

            raise Exception(
                "Invalid changed price contribution"
            )

        # -------------------------------------------------
        # Trend weight
        # -------------------------------------------------

        if breakdown["trend"]["weight"] != 0.4:

            raise Exception(
                "Trend weight was not changed"
            )

        if breakdown["trend"]["contribution"] != 38.96:

            raise Exception(
                "Invalid changed trend contribution"
            )

        # -------------------------------------------------
        # Momentum weight
        # -------------------------------------------------

        if breakdown["momentum"]["weight"] != 0.2:

            raise Exception(
                "Momentum weight was not changed"
            )

        if breakdown["momentum"]["contribution"] != 19.5:

            raise Exception(
                "Invalid changed momentum contribution"
            )

        # -------------------------------------------------
        # Weight sum
        # -------------------------------------------------

        weight_sum = (

            breakdown["price"]["weight"]
            +
            breakdown["trend"]["weight"]
            +
            breakdown["momentum"]["weight"]

        )

        if round(
            weight_sum,
            2
        ) != 1.0:

            raise Exception(
                f"Invalid changed weight sum: "
                f"{weight_sum}"
            )

        # -------------------------------------------------
        # Contribution sum
        # -------------------------------------------------

        contribution_sum = (

            breakdown["price"]["contribution"]
            +
            breakdown["trend"]["contribution"]
            +
            breakdown["momentum"]["contribution"]

        )

        if round(
            contribution_sum,
            2
        ) != 86.06:

            raise Exception(
                f"Invalid contribution sum: "
                f"{contribution_sum}"
            )

        # -------------------------------------------------
        # Final breakdown score
        # -------------------------------------------------

        if breakdown["final_score"] != 86.06:

            raise Exception(
                "Invalid changed final score"
            )


def run_default_test():

    scanner = create_scanner()

    results = scanner.scan()

    print_results(
        "SCANNER V2 DEFAULT TEST",
        results
    )

    validate_default_results(
        results
    )

    print(
        "DEFAULT WEIGHT TEST: PASS"
    )


def run_changed_weight_test():

    config = ScannerConfig()

    # -----------------------------------------------------
    # Changed ranking weights
    # -----------------------------------------------------

    config.price_weight = 0.4

    config.trend_weight = 0.4

    config.momentum_weight = 0.2

    scanner = create_scanner(
        config=config
    )

    results = scanner.scan()

    print_results(
        "SCANNER V2 CHANGED WEIGHT TEST",
        results
    )

    validate_changed_weight_results(
        results
    )

    print(
        "CHANGED WEIGHT TEST: PASS"
    )


def run_validation():

    print()

    print("=" * 60)

    print(
        "RANKING WEIGHT REGRESSION VALIDATION"
    )

    print("=" * 60)

    run_default_test()

    print()

    run_changed_weight_test()

    print()

    print("=" * 60)

    print(
        "VALIDATION FINISHED"
    )

    print("=" * 60)


if __name__ == "__main__":

    run_validation()