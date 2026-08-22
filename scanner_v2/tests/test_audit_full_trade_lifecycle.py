"""
Iran AI Trader Professional

Scanner V2

Sprint46-05

Audit + Full Trade Lifecycle Integration Test

Pipeline:

Trade Plan
    ↓
Validation
    ↓
Order Planning
    ↓
Position
    ↓
Portfolio Risk
    ↓
Execution Readiness
    ↓
Execution Control
    ↓
Audit
    ↓
Exit
    ↓
Risk Recalculation

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

from scanner_v2.execution_audit_engine import (
    ExecutionAuditEngine
)


def test_audit_full_trade_lifecycle():

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

    audit_engine = (
        ExecutionAuditEngine()
    )

    # =================================================
    # TEST1 — COMPLETE APPROVED TRADE
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
    # STEP 1 — VALIDATION
    # -------------------------------------------------

    validated = (
        validation_engine.validate_orders(
            [trade_plan]
        )
    )

    assert len(validated) == 1

    assert validated[0][
        "validation_status"
    ] == "READY"

    # -------------------------------------------------
    # STEP 2 — ORDER PLANNING
    # -------------------------------------------------

    orders = (
        order_engine.build_orders(
            [
                {
                    "symbol":
                        validated[0]["symbol"],

                    "signal":
                        validated[0]["signal"],

                    "capital":
                        validated[0]["capital"],

                    "price":
                        validated[0]["price"],

                    "allocation_percent":
                        validated[0][
                            "allocation_percent"
                        ]
                }
            ]
        )
    )

    assert len(orders) == 1

    order = orders[0]

    assert order[
        "status"
    ] == "READY"

    # -------------------------------------------------
    # STEP 3 — POSITION
    # -------------------------------------------------

    approved_plan = {

        "symbol":
            order["symbol"],

        "final_status":
            "READY",

        "entry_price":
            order["price"],

        "quantity":
            order["quantity"],

        "risk_reward":
            3.0,

        "risk_status":
            "LOW RISK"

    }

    positions = (
        position_engine.build(
            [approved_plan]
        )
    )

    assert len(positions) == 1

    position = positions[0]

    position["capital"] = (
        order["order_value"]
    )

    position["risk_status"] = (
        "LOW RISK"
    )

    assert position[
        "status"
    ] == "OPEN"

    # -------------------------------------------------
    # STEP 4 — PORTFOLIO RISK
    # -------------------------------------------------

    risk = risk_engine.evaluate(
        [position],
        total_capital
    )

    assert risk[
        "status"
    ] == "CONTROLLED"

    assert risk[
        "portfolio_exposure_percent"
    ] == 20.0

    # -------------------------------------------------
    # STEP 5 — EXECUTION READINESS
    # -------------------------------------------------

    execution_order = dict(
        order
    )

    execution_order[
        "validation_status"
    ] = "READY"

    execution_order[
        "risk_status"
    ] = "LOW RISK"

    execution_order[
        "gate_decision"
    ] = "ALLOW"

    execution_order[
        "execution_status"
    ] = "READY"

    readiness = (
        readiness_engine.evaluate(
            execution_order
        )
    )

    assert readiness[
        "execution_status"
    ] == "READY"

    assert readiness[
        "ready"
    ] is True

    # -------------------------------------------------
    # STEP 6 — EXECUTION CONTROL
    # -------------------------------------------------

    controlled_order = dict(
        execution_order
    )

    controlled_order[
        "execution_status"
    ] = readiness[
        "execution_status"
    ]

    controlled = (
        control_engine.control(
            controlled_order
        )
    )

    assert controlled[
        "execution_control"
    ] == "APPROVED"

    assert controlled[
        "approved"
    ] is True

    # -------------------------------------------------
    # STEP 7 — AUDIT
    # -------------------------------------------------

    audit_input = dict(
        execution_order
    )

    audit_input[
        "execution_control"
    ] = controlled[
        "execution_control"
    ]

    audit_input[
        "execution_reason"
    ] = controlled[
        "execution_reason"
    ]

    audit_input[
        "final_decision"
    ] = "APPROVED"

    audit_record = (
        audit_engine.record(
            audit_input
        )
    )

    assert audit_record is not None

    assert audit_record[
        "symbol"
    ] == "TEST1"

    assert audit_record[
        "validation_status"
    ] == "READY"

    assert audit_record[
        "risk_status"
    ] == "LOW RISK"

    assert audit_record[
        "gate_decision"
    ] == "ALLOW"

    assert audit_record[
        "execution_control"
    ] == "APPROVED"

    assert audit_record[
        "final_decision"
    ] == "APPROVED"

    assert audit_record[
        "broker_execution"
    ] is False

    # -------------------------------------------------
    # STEP 8 — TAKE PROFIT
    # -------------------------------------------------

    closed = (
        position_engine.update_price(
            position,
            position["take_profit"]
        )
    )

    assert closed[
        "status"
    ] == "CLOSED"

    assert closed[
        "exit_reason"
    ] == "TAKE PROFIT"

    # -------------------------------------------------
    # STEP 9 — RISK AFTER EXIT
    # -------------------------------------------------

    risk_after = (
        risk_engine.evaluate(
            position_engine.get_open_positions(),
            total_capital
        )
    )

    assert risk_after[
        "portfolio_exposure_percent"
    ] == 0.0

    assert risk_after[
        "invested_capital"
    ] == 0.0

    assert risk_after[
        "available_capital"
    ] == total_capital

    # =================================================
    # TEST2 — BLOCKED TRADE MUST BE AUDITED
    # =================================================

    blocked_order = {

        "symbol": "TEST2",

        "side": "BUY",

        "signal": "BUY",

        "price": 2000,

        "quantity": 10_000,

        "order_value": 20_000_000,

        "validation_status":
            "READY",

        "risk_status":
            "CRITICAL",

        "gate_decision":
            "BLOCK",

        "execution_status":
            "BLOCKED",

        "broker_execution":
            False

    }

    blocked_control = (
        control_engine.control(
            blocked_order
        )
    )

    assert blocked_control[
        "execution_control"
    ] == "BLOCKED"

    assert blocked_control[
        "approved"
    ] is False

    blocked_audit = dict(
        blocked_order
    )

    blocked_audit[
        "execution_control"
    ] = blocked_control[
        "execution_control"
    ]

    blocked_audit[
        "execution_reason"
    ] = blocked_control[
        "execution_reason"
    ]

    blocked_audit[
        "final_decision"
    ] = "BLOCKED"

    blocked_record = (
        audit_engine.record(
            blocked_audit
        )
    )

    assert blocked_record is not None

    assert blocked_record[
        "symbol"
    ] == "TEST2"

    assert blocked_record[
        "risk_status"
    ] == "CRITICAL"

    assert blocked_record[
        "gate_decision"
    ] == "BLOCK"

    assert blocked_record[
        "final_decision"
    ] == "BLOCKED"

    # -------------------------------------------------
    # AUDIT STATISTICS
    # -------------------------------------------------

    stats = (
        audit_engine.statistics()
    )

    assert stats[
        "total"
    ] == 2

    assert stats[
        "approved"
    ] == 1

    assert stats[
        "blocked"
    ] == 1

    assert stats[
        "broker_execution"
    ] is False

    # =================================================
    # OUTPUT
    # =================================================

    print()

    print("=" * 60)
    print(
        "AUDIT + FULL TRADE LIFECYCLE"
    )
    print("=" * 60)

    print(
        "TEST1 | Validation:",
        validated[0][
            "validation_status"
        ]
    )

    print(
        "TEST1 | Risk:",
        risk[
            "status"
        ]
    )

    print(
        "TEST1 | Execution:",
        controlled[
            "execution_control"
        ]
    )

    print(
        "TEST1 | Audit:",
        audit_record[
            "final_decision"
        ]
    )

    print(
        "TEST1 | Exit:",
        closed[
            "exit_reason"
        ]
    )

    print(
        "TEST1 | Exposure After Exit:",
        risk_after[
            "portfolio_exposure_percent"
        ],
        "%"
    )

    print()

    print(
        "TEST2 | Risk:",
        blocked_record[
            "risk_status"
        ]
    )

    print(
        "TEST2 | Gate:",
        blocked_record[
            "gate_decision"
        ]
    )

    print(
        "TEST2 | Audit:",
        blocked_record[
            "final_decision"
        ]
    )

    print()

    print(
        "Audit Total:",
        stats["total"]
    )

    print(
        "Audit Approved:",
        stats["approved"]
    )

    print(
        "Audit Blocked:",
        stats["blocked"]
    )

    print(
        "Broker Execution:",
        stats["broker_execution"]
    )

    print("=" * 60)