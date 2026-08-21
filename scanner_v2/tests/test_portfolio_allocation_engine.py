from scanner_v2.portfolio_allocation_engine import (
    PortfolioAllocationEngine
)


def test_portfolio_allocation_engine():

    engine = PortfolioAllocationEngine(
        max_positions=3,
        max_total_allocation=40
    )

    results = [

        {
            "symbol": "TEST1",
            "score": 98.54,
            "signal": "STRONG BUY",
            "risk_score": 100,
            "risk_status": "LOW RISK",
            "allocation_percent": 20.0
        },

        {
            "symbol": "TEST2",
            "score": 97.02,
            "signal": "BUY",
            "risk_score": 85.26,
            "risk_status": "LOW RISK",
            "allocation_percent": 11.94
        },

        {
            "symbol": "TEST3",
            "score": 95.01,
            "signal": "BUY",
            "risk_score": 80,
            "risk_status": "LOW RISK",
            "allocation_percent": 10.0
        },

        {
            "symbol": "TEST4",
            "score": 80,
            "signal": "WATCH",
            "risk_score": 90,
            "risk_status": "LOW RISK",
            "allocation_percent": 15.0
        },

        {
            "symbol": "TEST5",
            "score": 70,
            "signal": "BUY",
            "risk_score": 60,
            "risk_status": "HIGH RISK",
            "allocation_percent": 20.0
        }
    ]

    portfolio = engine.build(
        results
    )

    print()
    print("=" * 60)
    print("PORTFOLIO ALLOCATION ENGINE TEST")
    print("=" * 60)

    for item in portfolio:

        print(
            item["portfolio_rank"],
            item["symbol"],
            "| Signal:",
            item["signal"],
            "| Risk:",
            item["risk_status"],
            "| Allocation:",
            item[
                "final_allocation_percent"
            ],
            "%"
        )

    assert len(
        portfolio
    ) <= 3

    assert sum(
        item[
            "final_allocation_percent"
        ]
        for item in portfolio
    ) <= 40

    assert "TEST1" in [
        item["symbol"]
        for item in portfolio
    ]

    assert "TEST4" not in [
        item["symbol"]
        for item in portfolio
    ]

    assert "TEST5" not in [
        item["symbol"]
        for item in portfolio
    ]

    assert portfolio[0][
        "symbol"
    ] == "TEST1"