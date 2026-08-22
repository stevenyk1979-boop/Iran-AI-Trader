"""
Iran AI Trader Professional

Scanner V2

Sprint46-03

Full Trade Lifecycle V3 Integration Test

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
Risk Alert / Decision / Gate
    ↓
Execution Readiness
    ↓
Execution Control

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

from scanner_v2.execution_readiness_engine import (
    ExecutionReadinessEngine
)

from scanner_v2.execution_control_engine import (
    ExecutionControlEngine
)


def test_full_trade_lifecycle_v3():

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

    readiness_engine = (
        ExecutionReadinessEngine()
    )

    control_engine = (
        ExecutionControlEngine()
    )

    # =================================================
    # TEST1 — NORMAL TRADE
    # =================================================

    trade1 = {

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
    # Validation
    # -------------------------------------------------

    validated1 = (
        validation_engine.validate_orders(
            [trade1]
        )
    )

    assert len(validated1) == 1

    assert validated1[0][
        "validation_status"
    ] == "READY"

    # -------------------------------------------------
    # Order Planning
    # -------------------------------------------------

    orders1 = (
        order_engine.build_orders(
            [
                {
                    "symbol":
                        validated1[0]["symbol"],

                    "signal":
                        validated1[0]["signal"],

                    "capital":
                        validated1[0]["capital"],

                    "price":
                        validated1[0]["price"],

                    "allocation_percent":
                        validated1[0][
                            "allocation_percent"
                        ]
                }
            ]
        )
    )

    assert len(orders1) == 1

    order1 = orders1[0]

    assert order1[
        "status"
    ] == "READY"

    # -------------------------------------------------
    # Position
    # -------------------------------------------------

    plan1 = {

        "symbol": order1["symbol"],

        "final_status": "READY",

        "entry_price": order1["price"],

        "quantity": order1["quantity"],

        "risk_reward": 3.0,

        "risk_status": "LOW RISK"

    }

    positions1 = (
        position_engine.build(
            [plan1]
        )
    )

    assert len(positions1) == 1

    position1 = positions1[0]

    position1["capital"] = (
        order1["order_value"]
    )

    position1["risk_status"] = (
        "LOW RISK"
    )

    assert position1[
        "status"
    ] == "OPEN"

    # -------------------------------------------------
    # Portfolio Risk
    # -------------------------------------------------

    risk1 = risk_engine.evaluate(
        [position1],
        total_capital
    )

    assert risk1[
        "status"
    ] == "CONTROLLED"

    assert risk1[
        "portfolio_exposure_percent"
    ] == 20.0

    # -------------------------------------------------
    # Execution Readiness
    # -------------------------------------------------

    readiness_input1 = dict(
        order1
    )

    readiness_input1[
        "validation_status"
    ] = "READY"

    readiness_input1[
        "execution_status"
    ] = "READY"

    readiness_input1[
        "risk_status"
    ] = "LOW RISK"

    readiness_input1[
        "gate_decision"
    ] = "ALLOW"

    readiness1 = (
        readiness_engine.evaluate(
            readiness_input1
        )
    )

    assert readiness1[
        "execution_status"
    ] == "READY"

    assert readiness1[
        "ready"
    ] is True

    # -------------------------------------------------
    # Execution Control
    # -------------------------------------------------

    control_input1 = dict(
        readiness_input1
    )

    control_input1[
        "execution_status"
    ] = readiness1[
        "execution_status"
    ]

    control1 = (
        control_engine.control(
            control_input1
        )
    )

    assert control1[
        "execution_control"
    ] == "APPROVED"

    assert control1[
        "approved"
    ] is True

    # -------------------------------------------------
    # Take Profit
    # -------------------------------------------------

    closed1 = (
        position_engine.update_price(
            position1,
            position1["take_profit"]
        )
    )

    assert closed1[
        "status"
    ] == "CLOSED"

    assert closed1[
        "exit_reason"
    ] == "TAKE PROFIT"

    # -------------------------------------------------
    # Risk after exit
    # -------------------------------------------------

    risk_after1 = risk_engine.evaluate(
        position_engine.get_open_positions(),
        total_capital
    )

    assert risk_after1[
        "portfolio_exposure_percent"
    ] == 0.0

    assert risk_after1[
        "available_capital"
    ] == 100_000_000

    # =================================================
    # TEST2 — WARNING TRADE
    # =================================================

    warning_order = {

        "symbol": "TEST2",

        "side": "BUY",

        "signal": "BUY",

        "price": 2000,

        "capital": 11_940_000,

        "allocation_percent": 11.94,

        "quantity": 5_970,

        "order_value": 11_940_000,

        "status": "READY",

        "validation_status": "READY",

        "execution_status":
            "READY_WITH_WARNING",

        "gate_decision":
            "ALLOW_WITH_WARNING",

        "risk_status":
            "LOW RISK",

        "broker_execution": False

    }

    readiness2 = (
        readiness_engine.evaluate(
            warning_order
        )
    )

    assert readiness2[
        "execution_status"
    ] == "READY_WITH_WARNING"

    assert readiness2[
        "ready"
    ] is True

    control2 = (
        control_engine.control(
            warning_order
        )
    )

    assert control2[
        "execution_control"
    ] == "APPROVED_WITH_WARNING"

    assert control2[
        "approved"
    ] is True

    # =================================================
    # TEST3 — CRITICAL RISK
    # =================================================

    critical_order = {

        "symbol": "TEST3",

        "side": "BUY",

        "signal": "BUY",

        "price": 2000,

        "capital": 20_000_000,

        "quantity": 10_000,

        "order_value": 20_000_000,

        "status": "READY",

        "validation_status": "READY",

        "execution_status": "BLOCKED",

        "gate_decision": "BLOCK",

        "risk_status": "CRITICAL",

        "broker_execution": False

    }

    readiness3 = (
        readiness_engine.evaluate(
            critical_order
        )
    )

    assert readiness3[
        "execution_status"
    ] == "BLOCKED"

    assert readiness3[
        "ready"
    ] is False

    control3 = (
        control_engine.control(
            critical_order
        )
    )

    assert control3[
        "execution_control"
    ] == "BLOCKED"

    assert control3[
        "approved"
    ] is False

    # =================================================
    # TEST4 — INVALID ORDER VALUE
    # =================================================

    invalid_order = {

        "symbol": "TEST4",

        "side": "BUY",

        "signal": "BUY",

        "price": 1000,

        "quantity": 20_000,

        "order_value": 25_000_000,

        "status": "READY",

        "validation_status": "READY",

        "execution_status": "READY",

        "gate_decision": "ALLOW",

        "risk_status": "LOW RISK",

        "broker_execution": False

    }

    control4 = (
        control_engine.control(
            invalid_order
        )
    )

    assert control4[
        "execution_control"
    ] == "BLOCKED"

    assert control4[
        "execution_reason"
    ] == "ORDER_VALUE_MISMATCH"

    # =================================================
    # SAFETY
    # =================================================

    assert (
        control_engine.statistics()[
            "broker_execution"
        ]
        is False
    )

    # =================================================
    # OUTPUT
    # =================================================

    print()

    print("=" * 60)
    print(
        "FULL TRADE LIFECYCLE V3"
    )
    print("=" * 60)

    print(
        "TEST1 | Validation:",
        validated1[0][
            "validation_status"
        ]
    )

    print(
        "TEST1 | Order:",
        order1[
            "status"
        ]
    )

    print(
        "TEST1 | Position:",
        "OPEN"
    )

    print(
        "TEST1 | Risk:",
        risk1[
            "status"
        ]
    )

    print(
        "TEST1 | Readiness:",
        readiness1[
            "execution_status"
        ]
    )

    print(
        "TEST1 | Control:",
        control1[
            "execution_control"
        ]
    )

    print(
        "TEST1 | Exit:",
        closed1[
            "exit_reason"
        ]
    )

    print(
        "TEST1 | Exposure After Exit:",
        risk_after1[
            "portfolio_exposure_percent"
        ],
        "%"
    )

    print()

    print(
        "TEST2 | Readiness:",
        readiness2[
            "execution_status"
        ]
    )

    print(
        "TEST2 | Control:",
        control2[
            "execution_control"
        ]
    )

    print()

    print(
        "TEST3 | Readiness:",
        readiness3[
            "execution_status"
        ]
    )

    print(
        "TEST3 | Control:",
        control3[
            "execution_control"
        ]
    )

    print()

    print(
        "TEST4 | Control:",
        control4[
            "execution_control"
        ]
    )

    print("=" * 60)