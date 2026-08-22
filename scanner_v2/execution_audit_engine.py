"""
Iran AI Trader Professional

Scanner V2

Sprint46-04

Execution Audit Engine

Records the complete pre-execution decision path.

IMPORTANT:
This engine DOES NOT execute orders.
No broker connection.
No real order submission.
"""


from datetime import datetime


class ExecutionAuditEngine:

    def __init__(self):

        self.records = []

    # -------------------------------------------------
    # Create audit record
    # -------------------------------------------------

    def record(self, order):

        if not isinstance(order, dict):

            return None

        symbol = order.get(
            "symbol"
        )

        if not symbol:

            return None

        record = {

            "timestamp":
                datetime.now().isoformat(),

            "symbol":
                symbol,

            "signal":
                order.get(
                    "signal"
                ),

            "side":
                order.get(
                    "side",
                    "BUY"
                ),

            "price":
                self._number(
                    order.get(
                        "price",
                        order.get(
                            "entry_price",
                            0
                        )
                    )
                ),

            "quantity":
                self._integer(
                    order.get(
                        "quantity",
                        0
                    )
                ),

            "order_value":
                self._number(
                    order.get(
                        "order_value",
                        0
                    )
                ),

            "validation_status":
                order.get(
                    "validation_status",
                    "UNKNOWN"
                ),

            "risk_status":
                order.get(
                    "risk_status",
                    "UNKNOWN"
                ),

            "gate_decision":
                order.get(
                    "gate_decision",
                    "UNKNOWN"
                ),

            "execution_status":
                order.get(
                    "execution_status",
                    "UNKNOWN"
                ),

            "execution_control":
                order.get(
                    "execution_control",
                    "UNKNOWN"
                ),

            "final_decision":
                order.get(
                    "final_decision",
                    order.get(
                        "execution_control",
                        "UNKNOWN"
                    )
                ),

            "reason":
                order.get(
                    "execution_reason",
                    order.get(
                        "reason",
                        ""
                    )
                ),

            "broker_execution":
                order.get(
                    "broker_execution",
                    False
                )

        }

        self.records.append(
            record
        )

        return dict(
            record
        )

    # -------------------------------------------------
    # Record multiple orders
    # -------------------------------------------------

    def record_orders(self, orders):

        if not isinstance(
            orders,
            list
        ):

            return []

        results = []

        for order in orders:

            result = self.record(
                order
            )

            if result is not None:

                results.append(
                    result
                )

        return results

    # -------------------------------------------------
    # Get all records
    # -------------------------------------------------

    def get_records(self):

        return [
            dict(record)
            for record in self.records
        ]

    # -------------------------------------------------
    # Get records by symbol
    # -------------------------------------------------

    def get_symbol_records(
        self,
        symbol
    ):

        return [

            dict(record)

            for record in self.records

            if record.get(
                "symbol"
            ) == symbol

        ]

    # -------------------------------------------------
    # Get approved records
    # -------------------------------------------------

    def get_approved_records(self):

        return [

            dict(record)

            for record in self.records

            if record.get(
                "final_decision"
            ) in (
                "APPROVED",
                "ALLOW"
            )

        ]

    # -------------------------------------------------
    # Get warning records
    # -------------------------------------------------

    def get_warning_records(self):

        return [

            dict(record)

            for record in self.records

            if record.get(
                "final_decision"
            ) in (
                "APPROVED_WITH_WARNING",
                "ALLOW_WITH_WARNING"
            )

        ]

    # -------------------------------------------------
    # Get blocked records
    # -------------------------------------------------

    def get_blocked_records(self):

        return [

            dict(record)

            for record in self.records

            if record.get(
                "final_decision"
            ) in (
                "BLOCKED",
                "BLOCK"
            )

        ]

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(self):

        approved = len(
            self.get_approved_records()
        )

        warnings = len(
            self.get_warning_records()
        )

        blocked = len(
            self.get_blocked_records()
        )

        return {

            "total":
                len(
                    self.records
                ),

            "approved":
                approved,

            "warnings":
                warnings,

            "blocked":
                blocked,

            "broker_execution":
                False

        }

    # -------------------------------------------------
    # Clear audit history
    # -------------------------------------------------

    def clear(self):

        self.records = []

    # -------------------------------------------------
    # Safe conversion
    # -------------------------------------------------

    def _number(
        self,
        value
    ):

        try:

            return float(
                value
            )

        except Exception:

            return 0.0

    # -------------------------------------------------

    def _integer(
        self,
        value
    ):

        try:

            return int(
                value
            )

        except Exception:

            return 0