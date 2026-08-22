"""
Iran AI Trader Professional

Scanner V2

Sprint46-03

Portfolio Risk Alert Engine Test

No broker connection.
No real order execution.
"""


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

                "status": "INVALID",

                "stop_distance_percent": 0.0

            }

        current_price = self._number(
            position.get(
                "current_price",
                position.get(
                    "price",
                    0
                )
            )
        )

        stop_loss = self._number(
            position.get(
                "stop_loss",
                0
            )
        )

        position_status = position.get(
            "status",
            "OPEN"
        )

        if current_price <= 0:

            return {

                "status": "INVALID",

                "stop_distance_percent": 0.0

            }

        if stop_loss <= 0:

            return {

                "status": "INVALID",

                "stop_distance_percent": 0.0

            }

        # -------------------------------------------------
        # Already stopped
        # -------------------------------------------------

        if (
            current_price <=
            stop_loss
        ):

            return {

                "status": "STOPPED",

                "stop_distance_percent": 0.0

            }

        if position_status == "CLOSED":

            return {

                "status": "CLOSED",

                "stop_distance_percent":
                    round(
                        (
                            (
                                current_price
                                - stop_loss
                            )
                            / current_price
                        ) * 100,
                        2
                    )

            }

        # -------------------------------------------------
        # Distance to stop
        # -------------------------------------------------

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

        # -------------------------------------------------
        # Risk classification
        # -------------------------------------------------

        if (
            distance <=
            self.critical_threshold
        ):

            status = "CRITICAL"

        elif (
            distance <=
            self.warning_threshold
        ):

            status = "WARNING"

        else:

            status = "NORMAL"

        return {

            "status": status,

            "stop_distance_percent":
                distance

        }

    # -------------------------------------------------
    # Evaluate portfolio
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

        results = []

        for position in positions:

            result = self.evaluate(
                position
            )

            item = dict(
                position
            )

            item.update(
                result
            )

            results.append(
                item
            )

        return results


def test_portfolio_risk_alert_engine():

    engine = (
        PortfolioRiskAlertEngine(
            warning_threshold=10.0,
            critical_threshold=5.0
        )
    )

    positions = [

        {
            "symbol": "TEST1",
            "entry_price": 1000,
            "current_price": 1680,
            "stop_loss": 750,
            "status": "OPEN"
        },

        {
            "symbol": "TEST2",
            "entry_price": 2000,
            "current_price": 1600,
            "stop_loss": 1500,
            "status": "OPEN"
        },

        {
            "symbol": "TEST3",
            "entry_price": 1000,
            "current_price": 820,
            "stop_loss": 800,
            "status": "OPEN"
        },

        {
            "symbol": "TEST4",
            "entry_price": 1000,
            "current_price": 780,
            "stop_loss": 800,
            "status": "OPEN"
        }

    ]

    results = engine.evaluate_all(
        positions
    )

    assert len(results) == 4

    # -------------------------------------------------
    # TEST1
    # Distance = 55.36%
    # -------------------------------------------------

    assert (
        results[0]["status"]
        == "NORMAL"
    )

    assert (
        results[0][
            "stop_distance_percent"
        ]
        == 55.36
    )

    # -------------------------------------------------
    # TEST2
    # Distance = 6.25%
    # -------------------------------------------------

    assert (
        results[1]["status"]
        == "WARNING"
    )

    assert (
        results[1][
            "stop_distance_percent"
        ]
        == 6.25
    )

    # -------------------------------------------------
    # TEST3
    # Distance = 2.44%
    # -------------------------------------------------

    assert (
        results[2]["status"]
        == "CRITICAL"
    )

    assert (
        results[2][
            "stop_distance_percent"
        ]
        == 2.44
    )

    # -------------------------------------------------
    # TEST4
    # Price below stop
    # -------------------------------------------------

    assert (
        results[3]["status"]
        == "STOPPED"
    )

    assert (
        results[3][
            "stop_distance_percent"
        ]
        == 0.0
    )

    print(
        "============================================================"
    )

    print(
        "PORTFOLIO RISK ALERT ENGINE TEST"
    )

    print(
        "============================================================"
    )

    for result in results:

        print(
            result["symbol"],
            "| Price:",
            result["current_price"],
            "| Stop:",
            result["stop_loss"],
            "| Distance:",
            result["stop_distance_percent"],
            "%",
            "| Status:",
            result["status"]
        )

    print(
        "============================================================"
    )

    print(
        "PASSED"
    )