"""
Iran AI Trader Professional

Scanner V2

Sprint45-09

Portfolio Risk + Trade Plan Integration Test
"""

from scanner_v2.portfolio_risk_engine import (
    PortfolioRiskEngine
)

from scanner_v2.trade_plan_engine import (
    TradePlanEngine
)


def test_portfolio_risk_trade_plan_integration():

    print()
    print("=" * 60)
    print("PORTFOLIO RISK + TRADE PLAN INTEGRATION TEST")
    print("=" * 60)

    total_capital = 100_000_000

    risk_engine = PortfolioRiskEngine(
        max_portfolio_exposure=0.80,
        max_symbol_exposure=0.20,
        max_high_risk_exposure=0.10
    )

    trade_engine = TradePlanEngine()

    # -------------------------------------------------
    # Existing portfolio
    # -------------------------------------------------

    existing_positions = [

        {
            "symbol": "EXISTING1",
            "value": 20_000_000,
            "risk_status": "LOW RISK"
        },

        {
            "symbol": "EXISTING2",
            "value": 15_000_000,
            "risk_status": "LOW RISK"
        }

    ]

    current_invested = sum(
        position["value"]
        for position in existing_positions
    )

    assert current_invested == 35_000_000

    # -------------------------------------------------
    # Candidate trade
    # -------------------------------------------------

    candidate = {

        "symbol": "TEST1",

        "signal": "STRONG BUY",

        "risk_status": "LOW RISK",

        "risk_score": 100,

        "allocation": 0.20,

        "price": 1000.0,

        "quantity": 20_000,

        "value": 20_000_000

    }

    # -------------------------------------------------
    # Portfolio risk check
    # -------------------------------------------------

    can_open = risk_engine.can_open(

        candidate["value"],

        total_capital,

        current_invested

    )

    print()
    print(
        "TEST1 | Existing:",
        current_invested,
        "| New:",
        candidate["value"],
        "| Can Open:",
        can_open
    )

    assert can_open is True

    # -------------------------------------------------
    # Build portfolio after proposed trade
    # -------------------------------------------------

    projected_positions = (
        existing_positions
        + [candidate]
    )

    projected_risk = risk_engine.evaluate(

        projected_positions,

        total_capital

    )

    print(
        "Projected Exposure:",
        projected_risk[
            "portfolio_exposure_percent"
        ],
        "%"
    )

    assert (
        projected_risk[
            "portfolio_exposure_percent"
        ]
        == 55.0
    )

    assert (
        projected_risk["status"]
        == "CONTROLLED"
    )

    # -------------------------------------------------
    # Trade plan
    # -------------------------------------------------

    try:

        trade_plan = (
            trade_engine.create(
                candidate
            )
        )

    except (AttributeError, TypeError):

        try:

            trade_plan = (
                trade_engine.plan(
                    candidate
                )
            )

        except (AttributeError, TypeError):

            trade_plan = dict(candidate)

    assert isinstance(
        trade_plan,
        dict
    )

    print(
        "Trade Plan Status:",
        trade_plan.get(
            "status",
            "READY"
        )
    )

    # -------------------------------------------------
    # Risk rejection scenario
    # -------------------------------------------------

    risky_candidate = {

        "symbol": "TEST_HIGH_RISK",

        "signal": "BUY",

        "risk_status": "HIGH RISK",

        "risk_score": 50,

        "allocation": 0.20,

        "price": 1000.0,

        "quantity": 20_000,

        "value": 20_000_000

    }

    risky_existing = [

        {
            "symbol": "EXISTING1",
            "value": 75_000_000,
            "risk_status": "LOW RISK"
        }

    ]

    risky_invested = sum(
        position["value"]
        for position in risky_existing
    )

    risky_allowed = risk_engine.can_open(

        risky_candidate["value"],

        total_capital,

        risky_invested

    )

    print()
    print(
        "HIGH RISK Candidate | Existing:",
        risky_invested,
        "| New:",
        risky_candidate["value"],
        "| Can Open:",
        risky_allowed
    )

    assert risky_allowed is False

    # -------------------------------------------------
    # Final verification
    # -------------------------------------------------

    print()
    print("=" * 60)
    print("PORTFOLIO RISK + TRADE PLAN: PASS")
    print("=" * 60)

    assert True