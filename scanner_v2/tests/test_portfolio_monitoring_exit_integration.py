"""
Iran AI Trader Professional

Scanner V2

Sprint46-02

Portfolio Monitoring + Exit Management Integration Test

No broker connection.
No real order execution.
"""

from scanner_v2.portfolio_monitoring_engine import (
    PortfolioMonitoringEngine
)

from scanner_v2.exit_management_engine import (
    ExitManagementEngine
)


def test_portfolio_monitoring_exit_integration():

    monitoring_engine = (
        PortfolioMonitoringEngine()
    )

    exit_engine = (
        ExitManagementEngine()
    )

    positions = [

        {
            "symbol": "TEST1",
            "entry_price": 1000,
            "quantity": 20000,
            "stop_loss": 750,
            "take_profit": 1750,
            "status": "OPEN"
        },

        {
            "symbol": "TEST2",
            "entry_price": 2000,
            "quantity": 5970,
            "stop_loss": 1500,
            "take_profit": 3000,
            "status": "OPEN"
        },

        {
            "symbol": "TEST3",
            "entry_price": 1000,
            "quantity": 10000,
            "stop_loss": 800,
            "take_profit": 1500,
            "status": "OPEN"
        }

    ]

    prices = {

        "TEST1": 1680,

        "TEST2": 1800,

        "TEST3": 820

    }

    monitored = monitoring_engine.monitor(
        positions,
        prices
    )

    assert len(monitored) == 3

    # -------------------------------------------------
    # TEST1
    # -------------------------------------------------

    test1 = monitored[0]

    assert test1["symbol"] == "TEST1"

    assert test1["status"] == "OPEN"

    assert test1["pnl"] == 13600000

    assert test1["pnl_percent"] == 68.0

    assert (
        test1["target_distance_percent"]
        == 4.17
    )

    assert (
        test1["stop_distance_percent"]
        == 55.36
    )

    # -------------------------------------------------
    # TEST2
    # -------------------------------------------------

    test2 = monitored[1]

    assert test2["symbol"] == "TEST2"

    assert test2["status"] == "OPEN"

    assert test2["pnl"] == -1194000

    assert test2["pnl_percent"] == -10.0

    assert (
        test2["target_distance_percent"]
        == 66.67
    )

    assert (
        test2["stop_distance_percent"]
        == 16.67
    )

    # -------------------------------------------------
    # TEST3
    # Very close to stop
    # -------------------------------------------------

    test3 = monitored[2]

    assert test3["symbol"] == "TEST3"

    assert test3["status"] == "OPEN"

    # (820 - 1000) * 10000
    # = -1,800,000

    assert test3["pnl"] == -1800000

    assert test3["pnl_percent"] == -18.0

    assert (
        test3["stop_distance_percent"]
        == 2.44
    )

    # -------------------------------------------------
    # Exit Management evaluation
    # -------------------------------------------------

    exit_results = []

    for position in monitored:

        result = exit_engine.evaluate(
            position,
            position["current_price"]
        )

        exit_results.append(
            result
        )

    assert len(exit_results) == 3

    # TEST1 remains open
    assert (
        exit_results[0]["status"]
        == "OPEN"
    )

    # TEST2 remains open
    assert (
        exit_results[1]["status"]
        == "OPEN"
    )

    # TEST3 is still above stop
    assert (
        exit_results[2]["status"]
        == "OPEN"
    )

    # -------------------------------------------------
    # Portfolio summary
    # -------------------------------------------------

    assert (
        monitoring_engine.total_invested()
        == 41940000
    )

    # 33,600,000
    # +10,746,000
    # + 8,200,000
    # = 52,546,000

    assert (
        monitoring_engine.total_current_value()
        == 52546000
    )

    # 13,600,000
    # - 1,194,000
    # - 1,800,000
    # = 10,606,000

    assert (
        monitoring_engine.total_pnl()
        == 10606000
    )

    assert (
        monitoring_engine.total_pnl_percent()
        == 25.29
    )

    print(
        "============================================================"
    )

    print(
        "PORTFOLIO MONITORING + EXIT MANAGEMENT"
    )

    print(
        "============================================================"
    )

    for position, result in zip(
        monitored,
        exit_results
    ):

        print(
            position["symbol"],
            "| Price:",
            position["current_price"],
            "| P/L:",
            position["pnl"],
            "| P/L %:",
            position["pnl_percent"],
            "| Exit:",
            result["status"]
        )

    print(
        "------------------------------------------------------------"
    )

    print(
        "Invested:",
        monitoring_engine.total_invested()
    )

    print(
        "Current:",
        monitoring_engine.total_current_value()
    )

    print(
        "Total P/L:",
        monitoring_engine.total_pnl()
    )

    print(
        "P/L %:",
        monitoring_engine.total_pnl_percent()
    )

    print(
        "PASSED"
    )