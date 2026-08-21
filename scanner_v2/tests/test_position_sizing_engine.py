"""
Iran AI Trader Professional

Scanner V2

Sprint45-05

Position Sizing Engine Test
"""

from scanner_v2.position_sizing_engine import (
    PositionSizingEngine
)


def test_position_sizing_engine():

    engine = PositionSizingEngine(
        max_portfolio_percent=20
    )

    portfolio_value = 100_000_000

    results = [

        {
            "symbol": "TEST1",
            "score": 98.54,
            "signal": "STRONG BUY",
            "risk_score": 100,
            "risk_status": "LOW RISK"
        },

        {
            "symbol": "TEST2",
            "score": 85.0,
            "signal": "BUY",
            "risk_score": 85.26,
            "risk_status": "LOW RISK"
        },

        {
            "symbol": "TEST3",
            "score": 72.0,
            "signal": "WATCH",
            "risk_score": 67.2,
            "risk_status": "HIGH RISK"
        },

        {
            "symbol": "TEST4",
            "score": 55.0,
            "signal": "IGNORE",
            "risk_score": 44.35,
            "risk_status": "HIGH RISK"
        }
    ]


    sized = engine.evaluate_all(
        results,
        portfolio_value
    )


    print()
    print("=" * 60)
    print("POSITION SIZING ENGINE TEST")
    print("=" * 60)


    for item in sized:

        print(
            item["position_rank"],
            item["symbol"],
            "| Signal:",
            item["signal"],
            "| Risk:",
            item["risk_status"],
            "| Risk Score:",
            item["risk_score"],
            "| Allocation:",
            item["allocation_percent"],
            "%",
            "| Capital:",
            item["allocated_capital"]
        )


    # ---------------------------------------------
    # Basic validation
    # ---------------------------------------------

    assert len(
        sized
    ) == 4


    # ---------------------------------------------
    # TEST1
    #
    # STRONG BUY
    # LOW RISK
    # Risk Score = 100
    # Max allocation = 20%
    # ---------------------------------------------

    test1 = next(
        item
        for item in sized
        if item["symbol"] == "TEST1"
    )

    assert (
        test1["allocation_percent"]
        == 20.0
    )

    assert (
        test1["allocated_capital"]
        == 20_000_000
    )


    # ---------------------------------------------
    # TEST2
    #
    # BUY
    # LOW RISK
    # ---------------------------------------------

    test2 = next(
        item
        for item in sized
        if item["symbol"] == "TEST2"
    )

    assert (
        test2["allocation_percent"]
        == 11.94
    )

    assert (
        test2["allocated_capital"]
        == 11_940_000
    )


    # ---------------------------------------------
    # HIGH RISK positions
    # must receive zero allocation
    # ---------------------------------------------

    test3 = next(
        item
        for item in sized
        if item["symbol"] == "TEST3"
    )

    test4 = next(
        item
        for item in sized
        if item["symbol"] == "TEST4"
    )


    assert (
        test3["allocation_percent"]
        == 0.0
    )

    assert (
        test3["allocated_capital"]
        == 0.0
    )


    assert (
        test4["allocation_percent"]
        == 0.0
    )

    assert (
        test4["allocated_capital"]
        == 0.0
    )


    # ---------------------------------------------
    # Ranking
    # ---------------------------------------------

    assert (
        sized[0]["symbol"]
        == "TEST1"
    )

    assert (
        sized[1]["symbol"]
        == "TEST2"
    )


    # ---------------------------------------------
    # Statistics
    # ---------------------------------------------

    stats = engine.statistics()


    assert (
        stats["total"]
        == 4
    )

    assert (
        stats["allocated_capital"]
        == 31_940_000
    )

    assert (
        stats["positions_with_allocation"]
        == 2
    )