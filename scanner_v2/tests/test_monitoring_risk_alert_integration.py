
"""
Iran AI Trader Professional

Scanner V2

Sprint46-04

Portfolio Monitoring + Risk Alert Integration Test

No broker connection.
No real order execution.
"""

from scanner_v2.portfolio_monitoring_engine import (
    PortfolioMonitoringEngine
)


class PortfolioRiskAlertEngine:

    def __init__(
        self,
        warning_threshold=10.0,
        critical_threshold=5.0
    ):

        self.warning_threshold = float(
            warning_threshold
        )

        self.critical_threshold = float(
            critical_threshold
        )

    # -------------------------------------------------
    # Safe number
    # -------------------------------------------------

    def _number(
        self,
        value,
        default=0.0
    ):

        try:
            return float(value)

        except Exception:
            return float(default)

    # -------------------------------------------------
    # Evaluate one monitored position
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
                "risk_alert": "INVALID",
                "stop_distance_percent": 0.0
            }

        current_price = self._number(
            position.get(
                "current_price",
                0
            )
        )

        stop_loss = self._number(
            position.get(
                "stop_loss",
                0
            )
        )

        status = position.get(
            "status",
            "OPEN"
        )

        if current_price <= 0:

            return {
                "risk_alert": "INVALID",
                "stop_distance_percent": 0.0
            }

        if stop_loss <= 0:

            return {
                "risk_alert": "INVALID",
                "stop_distance_percent": 0.0
            }

        if status == "CLOSED":

            return {
                "risk_alert": "CLOSED",
                "stop_distance_percent": 0.0
            }

        if current_price <= stop_loss:

            return {
                "risk_alert": "STOPPED",
                "stop_distance_percent": 0.0
            }

        distance = (
            (
                current_price
                - stop_loss
            )
            / current_price
        ) * 100

        distance = round(
            distance,
            2
        )

        if (
            distance
            <= self.critical_threshold
        ):

            alert = "CRITICAL"

        elif (
            distance
            <= self.warning_threshold
        ):

            alert = "WARNING"

        else:

            alert = "NORMAL"

        return {
            "risk_alert": alert,
            "stop_distance_percent": distance
        }

    # -------------------------------------------------
    # Evaluate all
    # -------------------------------------------------

    def evaluate_all(
        self,
        positions
    ):

        results = []

        if not isinstance(
            positions,
            list
        ):

            return results

        for position in positions:

            alert = self.evaluate(
                position
            )

            result = dict(
                position
            )

            result.update(
                alert
            )

            results.append(
                result
            )

        return results


def test_monitoring_risk_alert_integration():

    monitoring_engine = (
        PortfolioMonitoringEngine()
    )

    alert_engine = (
        PortfolioRiskAlertEngine(
            warning_threshold=10.0,
            critical_threshold=5.0
        )
    )

    positions = [

        {
            "symbol": "TEST1",
            "entry_price": 1000,
            "quantity": 20000,
            "stop_loss": 750,
            "take_profit": 1750,
            "status": "OPEN"
        },

        {
            "symbol": "TEST2",
            "entry_price": 2000,
            "quantity": 5970,
            "stop_loss": 1500,
            "take_profit": 3000,
            "status": "OPEN"
        },

        {
            "symbol": "TEST3",
            "entry_price": 1000,
            "quantity": 10000,
            "stop_loss": 800,
            "take_profit": 1500,
            "status": "OPEN"
        },

        {
            "symbol": "TEST4",
            "entry_price": 1000,
            "quantity": 10000,
            "stop_loss": 800,
            "take_profit": 1500,
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
    # Monitoring
    # -------------------------------------------------

    monitored = monitoring_engine.monitor(
        positions,
        prices
    )

    assert len(
        monitored
    ) == 4

    # -------------------------------------------------
    # Risk alerts
    # -------------------------------------------------

    results = alert_engine.evaluate_all(
        monitored
    )

    assert len(
        results
    ) == 4

    # -------------------------------------------------
    # TEST1
    # -------------------------------------------------

    assert (
        results[0]["risk_alert"]
        == "NORMAL"
    )

    assert (
        results[0][
            "stop_distance_percent"
        ]
        == 55.36
    )

    assert (
        results[0]["pnl"]
        == 13600000
    )

    # -------------------------------------------------
    # TEST2
    # -------------------------------------------------

    assert (
        results[1]["risk_alert"]
        == "WARNING"
    )

    assert (
        results[1][
            "stop_distance_percent"
        ]
        == 6.25
    )

    assert (
        results[1]["pnl"]
        == -2388000
    )

    # -------------------------------------------------
    # TEST3
    # -------------------------------------------------

    assert (
        results[2]["risk_alert"]
        == "CRITICAL"
    )

    assert (
        results[2][
            "stop_distance_percent"
        ]
        == 2.44
    )

    assert (
        results[2]["pnl"]
        == -1800000
    )

    # -------------------------------------------------
    # TEST4
    # -------------------------------------------------

    assert (
        results[3]["risk_alert"]
        == "STOPPED"
    )

    assert (
        results[3][
            "stop_distance_percent"
        ]
        == 0.0
    )

    assert (
        results[3]["pnl"]
        == -2200000
    )

    # -------------------------------------------------
    # Portfolio totals
    # -------------------------------------------------

    # 20,000,000
    # + 11,940,000
    # + 10,000,000
    # + 10,000,000
    #
    # = 51,940,000

    assert (
        monitoring_engine.total_invested()
        == 51940000
    )

    # Expected from the current
    # PortfolioMonitoringEngine implementation.

    assert (
        monitoring_engine.total_current_value()
        == 59152000
    )

    # 59,152,000 - 51,940,000
    #
    # = 7,212,000

    assert (
        monitoring_engine.total_pnl()
        == 7212000
    )

    print(
        "============================================================"
    )

    print(
        "PORTFOLIO MONITORING + RISK ALERT INTEGRATION"
    )

    print(
        "============================================================"
    )

    for result in results:

        print(
            result["symbol"],
            "| Price:",
            result["current_price"],
            "| P/L:",
            result["pnl"],
            "| Alert:",
            result["risk_alert"]
        )

    print(
        "------------------------------------------------------------"
    )

    print(
        "Invested:",
        monitoring_engine.total_invested()
    )

    print(
        "Current:",
        monitoring_engine.total_current_value()
    )

    print(
        "Total P/L:",
        monitoring_engine.total_pnl()
    )

    print(
        "============================================================"
    )

    print(
        "PASSED"
    )

