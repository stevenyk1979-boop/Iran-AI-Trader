"""
Iran AI Trader Professional

Scanner V2

Sprint45-15

End-to-End Trade Lifecycle Integration Test

Pipeline:

Trade Plan
    ↓
Pre-Trade Validation
    ↓
Order Planning
    ↓
Position Management
    ↓
Portfolio Risk
    ↓
Position Exit
    ↓
Portfolio Risk Recalculation

IMPORTANT:
No broker connection.
No real order execution.
"""


from scanner_v2.pre_trade_validation_engine import (
    PreTradeValidationEngine
)

from scanner_v2.order_planning_engine import (
    OrderPlanningEngine
)

from scanner_v2.position_management_engine import (
    PositionManagementEngine
)

from scanner_v2.portfolio_risk_engine import (
    PortfolioRiskEngine
)


def test_end_to_end_trade_lifecycle():

    total_capital = 100_000_000

    validation_engine = (
        PreTradeValidationEngine()
    )

    order_engine = (
        OrderPlanningEngine(
            lot_size=1
        )
    )

    position_engine = (
        PositionManagementEngine()
    )

    risk_engine = (
        PortfolioRiskEngine(
            max_portfolio_exposure=0.80,
            max_symbol_exposure=0.20,
            max_high_risk_exposure=0.10
        )
    )

    # =================================================
    # TRADE 1
    # =================================================

    trade_plan = {

        "symbol": "TEST1",

        "signal": "STRONG BUY",

        "price": 1000,

        "capital": 20_000_000,

        "allocation_percent": 20.0,

        "quantity": 20_000,

        "order_value": 20_000_000,

        "status": "READY",

        "broker_execution": False
    }

    # -------------------------------------------------
    # STEP 1 — PRE-TRADE VALIDATION
    # -------------------------------------------------

    validated = (
        validation_engine.validate_orders(
            [trade_plan]
        )
    )

    assert len(validated) == 1

    assert validated[0][
        "symbol"
    ] == "TEST1"

    assert validated[0][
        "validation_status"
    ] == "READY"

    # -------------------------------------------------
    # STEP 2 — ORDER PLANNING
    # -------------------------------------------------

    portfolio_input = [

        {

            "symbol": validated[0][
                "symbol"
            ],

            "signal": validated[0][
                "signal"
            ],

            "capital": validated[0][
                "capital"
            ],

            "price": validated[0][
                "price"
            ],

            "allocation_percent":
                validated[0][
                    "allocation_percent"
                ]
        }
    ]

    orders = (
        order_engine.build_orders(
            portfolio_input
        )
    )

    assert len(orders) == 1

    order = orders[0]

    assert order[
        "symbol"
    ] == "TEST1"

    assert order[
        "status"
    ] == "READY"

    assert order[
        "quantity"
    ] == 20_000

    assert order[
        "order_value"
    ] == 20_000_000

    assert order[
        "broker_execution"
    ] is False

    # -------------------------------------------------
    # STEP 3 — POSITION MANAGEMENT
    # -------------------------------------------------
    #
    # PositionManagementEngine expects a Trade Plan,
    # so we create the minimal approved plan from
    # the validated order.
    # -------------------------------------------------

    approved_trade_plan = {

        "symbol": order[
            "symbol"
        ],

        "final_status": "READY",

        "entry_price": order[
            "price"
        ],

        "quantity": order[
            "quantity"
        ],

        "risk_reward": 3.0,

        "risk_status": "LOW RISK"
    }

    positions = (
        position_engine.build(
            [approved_trade_plan]
        )
    )

    assert len(positions) == 1

    position = positions[0]

    assert position[
        "symbol"
    ] == "TEST1"

    assert position[
        "status"
    ] == "OPEN"

    assert position[
        "entry_price"
    ] == 1000.0

    # PortfolioRiskEngine reads "capital",
    # so attach the approved position value.
    position[
        "capital"
    ] = order[
        "order_value"
    ]

    position[
        "risk_status"
    ] = "LOW RISK"

    # -------------------------------------------------
    # STEP 4 — INITIAL PORTFOLIO RISK
    # -------------------------------------------------

    risk_before_exit = (
        risk_engine.evaluate(
            [position],
            total_capital
        )
    )

    assert risk_before_exit[
        "status"
    ] == "CONTROLLED"

    assert risk_before_exit[
        "invested_capital"
    ] == 20_000_000

    assert risk_before_exit[
        "available_capital"
    ] == 80_000_000

    assert risk_before_exit[
        "portfolio_exposure_percent"
    ] == 20.0

    # -------------------------------------------------
    # STEP 5 — NORMAL PRICE MOVEMENT
    # -------------------------------------------------

    updated = (
        position_engine.update_price(
            position,
            1200
        )
    )

    assert updated[
        "status"
    ] == "OPEN"

    assert updated[
        "current_price"
    ] == 1200.0

    # -------------------------------------------------
    # STEP 6 — TAKE PROFIT
    # -------------------------------------------------

    target = position[
        "take_profit"
    ]

    closed = (
        position_engine.update_price(
            position,
            target
        )
    )

    assert closed[
        "status"
    ] == "CLOSED"

    assert closed[
        "exit_reason"
    ] == "TAKE PROFIT"

    # -------------------------------------------------
    # STEP 7 — CLOSED POSITION REMOVED
    # FROM ACTIVE PORTFOLIO EXPOSURE
    # -------------------------------------------------

    open_positions = (
        position_engine.get_open_positions()
    )

    assert len(open_positions) == 0

    risk_after_exit = (
        risk_engine.evaluate(
            open_positions,
            total_capital
        )
    )

    assert risk_after_exit[
        "status"
    ] == "CONTROLLED"

    assert risk_after_exit[
        "invested_capital"
    ] == 0.0

    assert risk_after_exit[
        "available_capital"
    ] == 100_000_000

    assert risk_after_exit[
        "portfolio_exposure_percent"
    ] == 0.0

    # =================================================
    # TRADE 2 — HIGH RISK REJECTION
    # =================================================

    high_risk_trade = {

        "symbol": "TEST2",

        "signal": "BUY",

        "price": 2000,

        "capital": 20_000_000,

        "allocation_percent": 20.0,

        "quantity": 10_000,

        "order_value": 20_000_000,

        "status": "READY",

        "broker_execution": False,

        "risk_status": "HIGH RISK"
    }

    # Validation itself should still pass the
    # structural order because HIGH RISK is handled
    # by the risk layer.
    validated_high_risk = (
        validation_engine.validate_orders(
            [high_risk_trade]
        )
    )

    assert len(
        validated_high_risk
    ) == 1

    # Portfolio risk must reject excessive
    # high-risk exposure.
    high_risk_position = {

        "symbol": "TEST2",

        "capital": 20_000_000,

        "risk_status": "HIGH RISK",

        "status": "OPEN"
    }

    high_risk_evaluation = (
        risk_engine.evaluate(
            [high_risk_position],
            total_capital
        )
    )

    assert high_risk_evaluation[
        "status"
    ] == "HIGH RISK EXPOSURE"

    assert high_risk_evaluation[
        "risk_exposure_percent"
    ] == 20.0

    # =================================================
    # OUTPUT
    # =================================================

    print()

    print(
        "=" * 60
    )

    print(
        "END-TO-END TRADE LIFECYCLE"
    )

    print(
        "=" * 60
    )

    print(
        "TEST1 | Validation:",
        validated[0][
            "validation_status"
        ]
    )

    print(
        "TEST1 | Order:",
        order[
            "status"
        ]
    )

    print(
        "TEST1 | Position:",
        "OPEN"
    )

    print(
        "TEST1 | Portfolio Exposure:",
        risk_before_exit[
            "portfolio_exposure_percent"
        ],
        "%"
    )

    print(
        "TEST1 | Exit:",
        closed[
            "exit_reason"
        ]
    )

    print(
        "TEST1 | Position:",
        closed[
            "status"
        ]
    )

    print(
        "TEST1 | Portfolio Exposure After Exit:",
        risk_after_exit[
            "portfolio_exposure_percent"
        ],
        "%"
    )

    print()

    print(
        "TEST2 | High Risk Protection:",
        high_risk_evaluation[
            "status"
        ]
    )

    print(
        "TEST2 | Risk Exposure:",
        high_risk_evaluation[
            "risk_exposure_percent"
        ],
        "%"
    )

    print(
        "=" * 60
    )