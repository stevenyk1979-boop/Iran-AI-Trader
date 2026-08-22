"""
Iran AI Trader Professional

Scanner V2

Sprint45-14

Position Management + Portfolio Risk
Integration Test

IMPORTANT:
This test does NOT connect to a broker.
"""


from scanner_v2.position_management_engine import (
    PositionManagementEngine
)

from scanner_v2.portfolio_risk_engine import (
    PortfolioRiskEngine
)


def test_position_portfolio_risk_integration():

    position_engine = PositionManagementEngine()

    risk_engine = PortfolioRiskEngine(
        max_portfolio_exposure=0.80,
        max_symbol_exposure=0.20,
        max_high_risk_exposure=0.10
    )

    total_capital = 100_000_000

    # -------------------------------------------------
    # STEP 1
    # Build approved trade plans
    # -------------------------------------------------

    trade_plans = [

        {
            "symbol": "TEST1",

            "final_status": "READY",

            "entry_price": 1000,

            "quantity": 20_000,

            "risk_reward": 3.0,

            "risk_status": "LOW RISK"
        },

        {
            "symbol": "TEST2",

            "final_status": "READY",

            "entry_price": 2000,

            "quantity": 10_000,

            "risk_reward": 2.0,

            "risk_status": "LOW RISK"
        }
    ]

    # -------------------------------------------------
    # STEP 2
    # Build positions
    # -------------------------------------------------

    positions = position_engine.build(
        trade_plans
    )

    assert len(positions) == 2

    for position in positions:

        assert position[
            "status"
        ] == "OPEN"

    # -------------------------------------------------
    # Add portfolio risk fields required by
    # PortfolioRiskEngine.
    # -------------------------------------------------

    positions[0][
        "capital"
    ] = 20_000_000

    positions[0][
        "risk_status"
    ] = "LOW RISK"

    positions[1][
        "capital"
    ] = 20_000_000

    positions[1][
        "risk_status"
    ] = "LOW RISK"

    # -------------------------------------------------
    # STEP 3
    # Evaluate current portfolio
    # -------------------------------------------------

    evaluation = risk_engine.evaluate(
        positions,
        total_capital
    )

    assert evaluation[
        "status"
    ] == "CONTROLLED"

    assert evaluation[
        "invested_capital"
    ] == 40_000_000

    assert evaluation[
        "available_capital"
    ] == 60_000_000

    assert evaluation[
        "portfolio_exposure_percent"
    ] == 40.0

    assert evaluation[
        "positions_count"
    ] == 2

    # -------------------------------------------------
    # STEP 4
    # New position within portfolio limit
    # -------------------------------------------------

    can_open = risk_engine.can_open(
        position_value=20_000_000,
        total_capital=total_capital,
        current_invested=40_000_000
    )

    assert can_open is True

    projected_exposure = (
        40_000_000
        + 20_000_000
    ) / total_capital

    assert projected_exposure == 0.60

    # -------------------------------------------------
    # STEP 5
    # New position exceeding portfolio limit
    # -------------------------------------------------

    can_open_large = risk_engine.can_open(
        position_value=50_000_000,
        total_capital=total_capital,
        current_invested=40_000_000
    )

    assert can_open_large is False

    # -------------------------------------------------
    # STEP 6
    # High-risk exposure protection
    # -------------------------------------------------

    high_risk_positions = [

        {

            "symbol": "HIGH1",

            "capital": 15_000_000,

            "risk_status": "HIGH RISK",

            "status": "OPEN"

        }
    ]

    high_risk_evaluation = (
        risk_engine.evaluate(
            high_risk_positions,
            total_capital
        )
    )

    assert high_risk_evaluation[
        "status"
    ] == "HIGH RISK EXPOSURE"

    assert high_risk_evaluation[
        "risk_exposure_percent"
    ] == 15.0

    # -------------------------------------------------
    # STEP 7
    # Position closes after take profit
    # Portfolio risk must reflect the closed
    # position as removed from active exposure.
    # -------------------------------------------------

    target = positions[0][
        "take_profit"
    ]

    closed_position = (
        position_engine.update_price(
            positions[0],
            target
        )
    )

    assert closed_position[
        "status"
    ] == "CLOSED"

    assert closed_position[
        "exit_reason"
    ] == "TAKE PROFIT"

    active_positions = (
        position_engine.get_open_positions()
    )

    # TEST2 remains open.
    assert len(active_positions) == 1

    assert active_positions[0][
        "symbol"
    ] == "TEST2"

    # -------------------------------------------------
    # STEP 8
    # Re-evaluate portfolio after exit.
    # -------------------------------------------------

    active_positions[0][
        "capital"
    ] = 20_000_000

    active_positions[0][
        "risk_status"
    ] = "LOW RISK"

    after_exit = risk_engine.evaluate(
        active_positions,
        total_capital
    )

    assert after_exit[
        "status"
    ] == "CONTROLLED"

    assert after_exit[
        "invested_capital"
    ] == 20_000_000

    assert after_exit[
        "available_capital"
    ] == 80_000_000

    assert after_exit[
        "portfolio_exposure_percent"
    ] == 20.0

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    statistics = risk_engine.statistics(
        after_exit
    )

    assert statistics[
        "status"
    ] == "CONTROLLED"

    assert statistics[
        "positions_count"
    ] == 1

    assert statistics[
        "available_capital"
    ] == 80_000_000

    # -------------------------------------------------
    # Output
    # -------------------------------------------------

    print()

    print(
        "=" * 60
    )

    print(
        "POSITION MANAGEMENT + PORTFOLIO RISK"
    )

    print(
        "=" * 60
    )

    print(
        "Initial Positions:",
        len(positions)
    )

    print(
        "Initial Invested:",
        evaluation[
            "invested_capital"
        ]
    )

    print(
        "Initial Exposure:",
        evaluation[
            "portfolio_exposure_percent"
        ],
        "%"
    )

    print()

    print(
        "New Position 20M:",
        can_open
    )

    print(
        "Projected Exposure:",
        projected_exposure * 100,
        "%"
    )

    print(
        "New Position 50M:",
        can_open_large
    )

    print()

    print(
        "Take Profit:",
        closed_position[
            "symbol"
        ],
        "| Status:",
        closed_position[
            "status"
        ],
        "| Exit:",
        closed_position[
            "exit_reason"
        ]
    )

    print()

    print(
        "After Exit Exposure:",
        after_exit[
            "portfolio_exposure_percent"
        ],
        "%"
    )

    print(
        "After Exit Available:",
        after_exit[
            "available_capital"
        ]
    )

    print()

    print(
        "High Risk Protection:",
        high_risk_evaluation[
            "status"
        ]
    )

    print(
        "=" * 60
    )