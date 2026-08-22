from scanner_v2.portfolio_monitoring_engine import (
    PortfolioMonitoringEngine
)


def test_portfolio_monitoring_engine():

    engine = PortfolioMonitoringEngine()

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

        "TEST1": 1200,

        "TEST2": 1800,

        "TEST3": 900

    }

    monitored = engine.monitor(
        positions,
        prices
    )

    assert len(monitored) == 3

    test1 = monitored[0]

    assert test1["status"] == "OPEN"

    assert test1["pnl"] == 4000000

    assert test1["pnl_percent"] == 20.0

    test2 = monitored[1]

    assert test2["pnl"] == -1194000

    assert test2["pnl_percent"] == -10.0

    test3 = monitored[2]

    assert test3["pnl"] == -1000000

    assert test3["pnl_percent"] == -10.0

    # Correct total P/L:
    # 4,000,000 - 1,194,000 - 1,000,000
    # = 1,806,000

    assert engine.total_pnl() == 1806000

    assert engine.total_invested() == 41940000

    # Correct current value:
    # 24,000,000 + 10,746,000 + 9,000,000
    # = 43,746,000

    assert engine.total_current_value() == 43746000

    assert engine.total_pnl_percent() == 4.31

    stats = engine.statistics()

    assert stats["total_positions"] == 3

    assert stats["open_positions"] == 3

    assert stats["profitable_positions"] == 1

    assert stats["losing_positions"] == 2

    print(
        "============================================================"
    )

    print(
        "PORTFOLIO MONITORING ENGINE TEST"
    )

    print(
        "============================================================"
    )

    for position in monitored:

        print(
            position["symbol"],
            "| Price:",
            position["current_price"],
            "| P/L:",
            position["pnl"],
            "| P/L %:",
            position["pnl_percent"],
            "| Status:",
            position["status"]
        )

    print(
        "------------------------------------------------------------"
    )

    print(
        "Invested:",
        engine.total_invested()
    )

    print(
        "Current:",
        engine.total_current_value()
    )

    print(
        "Total P/L:",
        engine.total_pnl()
    )

    print(
        "P/L %:",
        engine.total_pnl_percent()
    )

    print(
        "PASSED"
    )