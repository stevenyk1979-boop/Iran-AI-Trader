"""
Iran AI Trader Professional

Scanner V2

Sprint45-08

Portfolio Risk Engine Test
"""

from scanner_v2.portfolio_risk_engine import (
    PortfolioRiskEngine
)


def test_portfolio_risk_engine():

    print()
    print("=" * 60)
    print("PORTFOLIO RISK ENGINE TEST")
    print("=" * 60)

    engine = PortfolioRiskEngine()

    positions = [

        {
            "symbol": "TEST1",
            "value": 20_000_000,
            "risk_status": "LOW RISK"
        },

        {
            "symbol": "TEST2",
            "value": 15_000_000,
            "risk_status": "LOW RISK"
        },

        {
            "symbol": "TEST3",
            "value": 5_000_000,
            "risk_status": "HIGH RISK"
        }

    ]

    total_capital = 100_000_000

    result = engine.evaluate(
        positions,
        total_capital
    )

    print(
        "Status:",
        result["status"]
    )

    print(
        "Invested:",
        result["invested_capital"]
    )

    print(
        "Available:",
        result["available_capital"]
    )

    print(
        "Exposure:",
        result[
            "portfolio_exposure_percent"
        ],
        "%"
    )

    print(
        "High Risk Exposure:",
        result[
            "risk_exposure_percent"
        ],
        "%"
    )

    assert (
        result["status"]
        == "CONTROLLED"
    )

    assert (
        result["invested_capital"]
        == 40_000_000
    )

    assert (
        result["available_capital"]
        == 60_000_000
    )

    assert (
        result["portfolio_exposure_percent"]
        == 40.0
    )

    # -------------------------------------------------
    # Portfolio overexposure
    # -------------------------------------------------

    overexposed = engine.evaluate(

        [
            {
                "symbol": "TEST1",
                "value": 85_000_000,
                "risk_status": "LOW RISK"
            }
        ],

        100_000_000
    )

    assert (
        overexposed["status"]
        == "OVEREXPOSED"
    )

    # -------------------------------------------------
    # Symbol overexposure
    # -------------------------------------------------

    symbol_overexposed = engine.evaluate(

        [
            {
                "symbol": "TEST1",
                "value": 30_000_000,
                "risk_status": "LOW RISK"
            }
        ],

        100_000_000
    )

    assert (
        symbol_overexposed["status"]
        == "SYMBOL OVEREXPOSED"
    )

    # -------------------------------------------------
    # High risk exposure
    # -------------------------------------------------

    high_risk = engine.evaluate(

        [
            {
                "symbol": "TEST1",
                "value": 15_000_000,
                "risk_status": "HIGH RISK"
            }
        ],

        100_000_000
    )

    assert (
        high_risk["status"]
        == "HIGH RISK EXPOSURE"
    )

    # -------------------------------------------------
    # Can open position
    # -------------------------------------------------

    assert (
        engine.can_open(
            10_000_000,
            100_000_000,
            50_000_000
        )
        is True
    )

    assert (
        engine.can_open(
            40_000_000,
            100_000_000,
            50_000_000
        )
        is False
    )

    print()
    print("PORTFOLIO RISK ENGINE: PASS")
    print("=" * 60)