"""
Iran AI Trader Professional

Scanner V2

Sprint46-04

Execution Audit Engine Test
"""


from scanner_v2.execution_audit_engine import (
    ExecutionAuditEngine
)


def test_execution_audit_engine():

    engine = (
        ExecutionAuditEngine()
    )

    orders = [

        {
            "symbol": "TEST1",
            "signal": "STRONG BUY",
            "side": "BUY",
            "price": 1000,
            "quantity": 20_000,
            "order_value": 20_000_000,
            "validation_status": "READY",
            "risk_status": "LOW RISK",
            "gate_decision": "ALLOW",
            "execution_status": "READY",
            "execution_control": "APPROVED",
            "execution_reason":
                "FINAL_EXECUTION_CHECKS_PASSED",
            "broker_execution": False
        },

        {
            "symbol": "TEST2",
            "signal": "BUY",
            "side": "BUY",
            "price": 2000,
            "quantity": 5_970,
            "order_value": 11_940_000,
            "validation_status": "READY",
            "risk_status": "LOW RISK",
            "gate_decision":
                "ALLOW_WITH_WARNING",
            "execution_status":
                "READY_WITH_WARNING",
            "execution_control":
                "APPROVED_WITH_WARNING",
            "execution_reason":
                "EXECUTION_WARNING",
            "broker_execution": False
        },

        {
            "symbol": "TEST3",
            "signal": "BUY",
            "side": "BUY",
            "price": 2000,
            "quantity": 10_000,
            "order_value": 20_000_000,
            "validation_status": "READY",
            "risk_status": "CRITICAL",
            "gate_decision": "BLOCK",
            "execution_status": "BLOCKED",
            "execution_control": "BLOCKED",
            "execution_reason":
                "RISK_GATE_BLOCKED",
            "broker_execution": False
        }

    ]

    records = (
        engine.record_orders(
            orders
        )
    )

    assert len(records) == 3

    # -------------------------------------------------
    # TEST1
    # -------------------------------------------------

    test1 = records[0]

    assert test1[
        "symbol"
    ] == "TEST1"

    assert test1[
        "validation_status"
    ] == "READY"

    assert test1[
        "risk_status"
    ] == "LOW RISK"

    assert test1[
        "gate_decision"
    ] == "ALLOW"

    assert test1[
        "execution_status"
    ] == "READY"

    assert test1[
        "execution_control"
    ] == "APPROVED"

    assert test1[
        "final_decision"
    ] == "APPROVED"

    # -------------------------------------------------
    # TEST2
    # -------------------------------------------------

    test2 = records[1]

    assert test2[
        "execution_control"
    ] == "APPROVED_WITH_WARNING"

    assert test2[
        "final_decision"
    ] == "APPROVED_WITH_WARNING"

    # -------------------------------------------------
    # TEST3
    # -------------------------------------------------

    test3 = records[2]

    assert test3[
        "risk_status"
    ] == "CRITICAL"

    assert test3[
        "execution_control"
    ] == "BLOCKED"

    assert test3[
        "final_decision"
    ] == "BLOCKED"

    # -------------------------------------------------
    # Symbol lookup
    # -------------------------------------------------

    symbol_records = (
        engine.get_symbol_records(
            "TEST1"
        )
    )

    assert len(
        symbol_records
    ) == 1

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    stats = (
        engine.statistics()
    )

    assert stats[
        "total"
    ] == 3

    assert stats[
        "approved"
    ] == 1

    assert stats[
        "warnings"
    ] == 1

    assert stats[
        "blocked"
    ] == 1

    assert stats[
        "broker_execution"
    ] is False

    # -------------------------------------------------
    # Output
    # -------------------------------------------------

    print()

    print("=" * 60)
    print(
        "EXECUTION AUDIT ENGINE TEST"
    )
    print("=" * 60)

    for record in records:

        print(
            record["symbol"],
            "| Validation:",
            record["validation_status"],
            "| Risk:",
            record["risk_status"],
            "| Gate:",
            record["gate_decision"],
            "| Control:",
            record["execution_control"],
            "| Final:",
            record["final_decision"]
        )

    print("-" * 60)

    print(
        "Total:",
        stats["total"]
    )

    print(
        "Approved:",
        stats["approved"]
    )

    print(
        "Warnings:",
        stats["warnings"]
    )

    print(
        "Blocked:",
        stats["blocked"]
    )

    print(
        "Broker Execution:",
        stats["broker_execution"]
    )

    print("=" * 60)