from scanner_v2.exit_management_engine import (
    ExitManagementEngine
)


def test_exit_management_engine():

    engine = ExitManagementEngine()

    position = {
        "symbol": "TEST1",
        "entry_price": 1000,
        "stop_loss": 750,
        "take_profit": 1500,
        "trailing_stop": 1200,
        "status": "OPEN"
    }

    # -------------------------------------------------
    # Position remains open
    # -------------------------------------------------

    result = engine.evaluate(
        position,
        1250
    )

    assert result["status"] == "OPEN"

    # -------------------------------------------------
    # Trailing stop
    # -------------------------------------------------

    position["status"] = "OPEN"

    result = engine.evaluate(
        position,
        1190
    )

    assert result["status"] == "CLOSED"

    assert (
        result["exit_reason"]
        == "TRAILING STOP"
    )

    # -------------------------------------------------
    # Take profit
    # -------------------------------------------------

    position["status"] = "OPEN"

    result = engine.evaluate(
        position,
        1500
    )

    assert result["status"] == "CLOSED"

    assert (
        result["exit_reason"]
        == "TAKE PROFIT"
    )

    # -------------------------------------------------
    # Stop loss
    # -------------------------------------------------

    position["status"] = "OPEN"

    result = engine.evaluate(
        position,
        700
    )

    assert result["status"] == "CLOSED"

    assert (
        result["exit_reason"]
        == "STOP LOSS"
    )

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    stats = engine.statistics()

    assert stats["closed_count"] == 3

    print("=" * 60)
    print("EXIT MANAGEMENT ENGINE TEST")
    print("=" * 60)

    print(
        "Open test: PASS"
    )

    print(
        "Trailing stop: PASS"
    )

    print(
        "Take profit: PASS"
    )

    print(
        "Stop loss: PASS"
    )

    print(
        "Closed:",
        stats["closed_count"]
    )