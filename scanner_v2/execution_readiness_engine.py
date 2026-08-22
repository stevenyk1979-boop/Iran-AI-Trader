"""
Iran AI Trader Professional

Scanner V2

Sprint46-01

Execution Readiness Engine

Determines whether an approved order is ready
for a future execution layer.

IMPORTANT:
This engine DOES NOT execute orders.
No broker connection.
No real order submission.
"""


class ExecutionReadinessEngine:

    # -------------------------------------------------
    # Initialization
    # -------------------------------------------------

    def __init__(self):

        self.ready_orders = []

        self.warning_orders = []

        self.blocked_orders = []

    # -------------------------------------------------
    # Validate one order
    # -------------------------------------------------

    def evaluate(self, order):

        if not isinstance(order, dict):

            return {
                "execution_status": "BLOCKED",
                "execution_reason": "INVALID_ORDER",
                "ready": False
            }

        errors = []

        symbol = order.get(
            "symbol"
        )

        quantity = order.get(
            "quantity",
            0
        )

        order_value = order.get(
            "order_value",
            0
        )

        status = order.get(
            "status",
            "UNKNOWN"
        )

        gate_decision = order.get(
            "gate_decision",
            order.get(
                "decision",
                "BLOCK"
            )
        )

        validation_status = order.get(
            "validation_status",
            "UNKNOWN"
        )

        broker_execution = order.get(
            "broker_execution",
            False
        )

        risk_status = order.get(
            "risk_status",
            "UNKNOWN"
        )

        # -------------------------------------------------
        # Symbol
        # -------------------------------------------------

        if not symbol:

            errors.append(
                "MISSING_SYMBOL"
            )

        # -------------------------------------------------
        # Quantity
        # -------------------------------------------------

        try:

            if int(quantity) <= 0:

                errors.append(
                    "INVALID_QUANTITY"
                )

        except Exception:

            errors.append(
                "INVALID_QUANTITY"
            )

        # -------------------------------------------------
        # Order value
        # -------------------------------------------------

        try:

            if float(order_value) <= 0:

                errors.append(
                    "INVALID_ORDER_VALUE"
                )

        except Exception:

            errors.append(
                "INVALID_ORDER_VALUE"
            )

        # -------------------------------------------------
        # Validation
        # -------------------------------------------------

        if validation_status not in (
            "READY",
            "VALID",
            "PASSED"
        ):

            errors.append(
                "VALIDATION_NOT_READY"
            )

        # -------------------------------------------------
        # Trade plan / order status
        # -------------------------------------------------

        if status != "READY":

            errors.append(
                "ORDER_NOT_READY"
            )

        # -------------------------------------------------
        # Risk gate
        # -------------------------------------------------

        if gate_decision == "BLOCK":

            errors.append(
                "RISK_GATE_BLOCKED"
            )

        # -------------------------------------------------
        # Broker safety
        # -------------------------------------------------

        if broker_execution is not False:

            errors.append(
                "BROKER_EXECUTION_ENABLED"
            )

        # -------------------------------------------------
        # Hard risk protection
        # -------------------------------------------------

        if risk_status in (
            "HIGH RISK",
            "EXTREME RISK",
            "CRITICAL",
            "STOPPED"
        ):

            errors.append(
                "RISK_STATUS_BLOCKED"
            )

        # -------------------------------------------------
        # Final decision
        # -------------------------------------------------

        if errors:

            result = {

                "symbol": symbol,

                "execution_status": "BLOCKED",

                "execution_reason":
                    errors[0],

                "ready": False,

                "errors": errors

            }

            self.blocked_orders.append(
                result
            )

            return result

        # -------------------------------------------------
        # Warning gate
        # -------------------------------------------------

        if gate_decision == "ALLOW_WITH_WARNING":

            result = {

                "symbol": symbol,

                "execution_status":
                    "READY_WITH_WARNING",

                "execution_reason":
                    "RISK_WARNING",

                "ready": True,

                "errors": [],

                "warning": True

            }

            self.warning_orders.append(
                result
            )

            return result

        # -------------------------------------------------
        # Fully ready
        # -------------------------------------------------

        result = {

            "symbol": symbol,

            "execution_status": "READY",

            "execution_reason":
                "ALL_EXECUTION_CHECKS_PASSED",

            "ready": True,

            "errors": [],

            "warning": False

        }

        self.ready_orders.append(
            result
        )

        return result

    # -------------------------------------------------
    # Evaluate multiple orders
    # -------------------------------------------------

    def evaluate_orders(self, orders):

        self.ready_orders = []

        self.warning_orders = []

        self.blocked_orders = []

        if not isinstance(
            orders,
            list
        ):

            return []

        results = []

        for order in orders:

            results.append(
                self.evaluate(
                    order
                )
            )

        return results

    # -------------------------------------------------
    # Ready orders
    # -------------------------------------------------

    def get_ready_orders(self):

        return list(
            self.ready_orders
        )

    # -------------------------------------------------
    # Warning orders
    # -------------------------------------------------

    def get_warning_orders(self):

        return list(
            self.warning_orders
        )

    # -------------------------------------------------
    # Blocked orders
    # -------------------------------------------------

    def get_blocked_orders(self):

        return list(
            self.blocked_orders
        )

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(self):

        return {

            "ready":
                len(
                    self.ready_orders
                ),

            "ready_with_warning":
                len(
                    self.warning_orders
                ),

            "blocked":
                len(
                    self.blocked_orders
                ),

            "total":
                (
                    len(self.ready_orders)
                    +
                    len(self.warning_orders)
                    +
                    len(self.blocked_orders)
                ),

            "broker_execution":
                False

        }