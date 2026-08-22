
"""
Iran AI Trader Professional

Scanner V2

Sprint46-05

Risk Alert + Decision Integration Test

No broker connection.
No real order execution.
"""


from scanner_v2.portfolio_monitoring_engine import (
    PortfolioMonitoringEngine
)


class RiskAlertDecisionFilter:

    BLOCKED_ALERTS = {
        "CRITICAL",
        "STOPPED",
        "CLOSED",
        "INVALID"
    }

    WARNING_ALERTS = {
        "WARNING"
    }

    ALLOWED_ALERTS = {
        "NORMAL"
    }

    # -------------------------------------------------
    # Evaluate one position
    # -------------------------------------------------

    def evaluate(
        self,
        position
    ):

        if not isinstance(
            position,
            dict
        ):

            return {
                "decision": "BLOCK",
                "reason": "INVALID_POSITION"
            }

        alert = position.get(
            "risk_alert",
            "INVALID"
        )

        symbol = position.get(
            "symbol",
            "UNKNOWN"
        )

        # -------------------------------------------------
        # Critical / stopped / closed
        # -------------------------------------------------

        if alert in self.BLOCKED_ALERTS:

            return {

                "symbol": symbol,

                "decision": "BLOCK",

                "reason":
                    "RISK_ALERT_" + alert

            }

        # -------------------------------------------------
        # Warning
        # -------------------------------------------------

        if alert in self.WARNING_ALERTS:

            return {

                "symbol": symbol,

                "decision":
                    "ALLOW_WITH_WARNING",

                "reason":
                    "RISK_WARNING"

            }

        # -------------------------------------------------
        # Normal
        # -------------------------------------------------

        if alert in self.ALLOWED_ALERTS:

            return {

                "symbol": symbol,

                "decision": "ALLOW",

                "reason":
                    "RISK_NORMAL"

            }

        # -------------------------------------------------
        # Unknown alert
        # -------------------------------------------------

        return {

            "symbol": symbol,

            "decision": "BLOCK",

            "reason":
                "UNKNOWN_RISK_ALERT"

        }


    # -------------------------------------------------
    # Evaluate all positions
    # -------------------------------------------------

    def evaluate_all(
        self,
        positions
    ):

        if not isinstance(
            positions,
            list
        ):

            return []

        return [

            self.evaluate(
                position
            )

            for position in positions

        ]


def test_risk_alert_decision_integration():

    monitoring_engine = (
        PortfolioMonitoringEngine()
    )

    alert_filter = (
        RiskAlertDecisionFilter()
    )

    positions = [

        {
            "symbol": "TEST1",
            "entry_price": 1000,
            "quantity": 20000,
            "stop_loss": 750,
            "status": "OPEN"
        },

        {
            "symbol": "TEST2",
            "entry_price": 2000,
            "quantity": 5970,
            "stop_loss": 1500,
            "status": "OPEN"
        },

        {
            "symbol": "TEST3",
            "entry_price": 1000,
            "quantity": 10000,
            "stop_loss": 800,
            "status": "OPEN"
        },

        {
            "symbol": "TEST4",
            "entry_price": 1000,
            "quantity": 10000,
            "stop_loss": 800,
            "status": "OPEN"
        }

    ]

    prices = {

        "TEST1": 1680,
        "TEST2": 1600,
        "TEST3": 820,
        "TEST4": 780

    }

    # -------------------------------------------------
    # Monitor
    # -------------------------------------------------

    monitored = monitoring_engine.monitor(
        positions,
        prices
    )

    assert len(
        monitored
    ) == 4

    # -------------------------------------------------
    # Attach risk alerts
    # -------------------------------------------------

    alerts = []

    for position in monitored:

        current_price = float(
            position.get(
                "current_price",
                0
            )
        )

        stop_loss = float(
            position.get(
                "stop_loss",
                0
            )
        )

        if current_price <= stop_loss:

            risk_alert = "STOPPED"

        else:

            distance = (
                (
                    current_price
                    - stop_loss
                )
                / current_price
            ) * 100

            if distance <= 5:

                risk_alert = "CRITICAL"

            elif distance <= 10:

                risk_alert = "WARNING"

            else:

                risk_alert = "NORMAL"

        item = dict(
            position
        )

        item[
            "risk_alert"
        ] = risk_alert

        alerts.append(
            item
        )

    # -------------------------------------------------
    # Decision filter
    # -------------------------------------------------

    decisions = (
        alert_filter.evaluate_all(
            alerts
        )
    )

    assert len(
        decisions
    ) == 4

    # TEST1 → NORMAL
    assert (
        decisions[0]["decision"]
        == "ALLOW"
    )

    assert (
        decisions[0]["reason"]
        == "RISK_NORMAL"
    )

    # TEST2 → WARNING
    assert (
        decisions[1]["decision"]
        == "ALLOW_WITH_WARNING"
    )

    assert (
        decisions[1]["reason"]
        == "RISK_WARNING"
    )

    # TEST3 → CRITICAL
    assert (
        decisions[2]["decision"]
        == "BLOCK"
    )

    assert (
        decisions[2]["reason"]
        == "RISK_ALERT_CRITICAL"
    )

    # TEST4 → STOPPED
    assert (
        decisions[3]["decision"]
        == "BLOCK"
    )

    assert (
        decisions[3]["reason"]
        == "RISK_ALERT_STOPPED"
    )

    print(
        "============================================================"
    )

    print(
        "RISK ALERT + DECISION INTEGRATION"
    )

    print(
        "============================================================"
    )

    for decision in decisions:

        print(
            decision["symbol"],
            "| Decision:",
            decision["decision"],
            "| Reason:",
            decision["reason"]
        )

    print(
        "============================================================"
    )

    print(
        "PASSED"
    )

