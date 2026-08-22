
"""
Iran AI Trader Professional

Scanner V2

Sprint46-06

Risk Alert Decision Engine

Converts portfolio risk alerts into
standardized trading decisions.

No broker connection.
No real order execution.
"""


class RiskAlertDecisionEngine:

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

                "symbol": "UNKNOWN",

                "decision": "BLOCK",

                "reason":
                    "INVALID_POSITION"

            }

        symbol = position.get(
            "symbol",
            "UNKNOWN"
        )

        alert = position.get(
            "risk_alert",
            "INVALID"
        )

        # -------------------------------------------------
        # Blocked
        # -------------------------------------------------

        if alert in self.BLOCKED_ALERTS:

            return {

                "symbol": symbol,

                "risk_alert": alert,

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

                "risk_alert": alert,

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

                "risk_alert": alert,

                "decision": "ALLOW",

                "reason":
                    "RISK_NORMAL"

            }

        # -------------------------------------------------
        # Unknown
        # -------------------------------------------------

        return {

            "symbol": symbol,

            "risk_alert": alert,

            "decision": "BLOCK",

            "reason":
                "UNKNOWN_RISK_ALERT"

        }

    # -------------------------------------------------
    # Evaluate all
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

    # -------------------------------------------------
    # Allowed positions
    # -------------------------------------------------

    def get_allowed(
        self,
        positions
    ):

        return [

            result

            for result in self.evaluate_all(
                positions
            )

            if result.get(
                "decision"
            ) == "ALLOW"

        ]

    # -------------------------------------------------
    # Warning positions
    # -------------------------------------------------

    def get_warning(
        self,
        positions
    ):

        return [

            result

            for result in self.evaluate_all(
                positions
            )

            if result.get(
                "decision"
            ) == "ALLOW_WITH_WARNING"

        ]

    # -------------------------------------------------
    # Blocked positions
    # -------------------------------------------------

    def get_blocked(
        self,
        positions
    ):

        return [

            result

            for result in self.evaluate_all(
                positions
            )

            if result.get(
                "decision"
            ) == "BLOCK"

        ]

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(
        self,
        positions
    ):

        results = self.evaluate_all(
            positions
        )

        return {

            "total": len(
                results
            ),

            "allowed": len(
                [
                    item
                    for item in results
                    if item.get(
                        "decision"
                    ) == "ALLOW"
                ]
            ),

            "warning": len(
                [
                    item
                    for item in results
                    if item.get(
                        "decision"
                    )
                    == "ALLOW_WITH_WARNING"
                ]
            ),

            "blocked": len(
                [
                    item
                    for item in results
                    if item.get(
                        "decision"
                    ) == "BLOCK"
                ]
            )

        }

