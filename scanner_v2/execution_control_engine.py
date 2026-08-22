"""
Iran AI Trader Professional

Scanner V2

Sprint46-02

Execution Control Engine

Final safety layer before future broker execution.

IMPORTANT:
This engine DOES NOT execute orders.
No broker connection.
No real order submission.
"""


class ExecutionControlEngine:

    def __init__(self):

        self.approved_orders = []
        self.warning_orders = []
        self.blocked_orders = []

    # -------------------------------------------------
    # Control one order
    # -------------------------------------------------

    def control(self, order):

        if not isinstance(order, dict):

            return {
                "execution_control": "BLOCKED",
                "execution_reason": "INVALID_ORDER",
                "approved": False
            }

        errors = []

        symbol = order.get(
            "symbol"
        )

        quantity = order.get(
            "quantity",
            0
        )

        price = order.get(
            "price",
            order.get(
                "entry_price",
                0
            )
        )

        order_value = order.get(
            "order_value",
            0
        )

        execution_status = order.get(
            "execution_status",
            "BLOCKED"
        )

        broker_execution = order.get(
            "broker_execution",
            False
        )

        side = order.get(
            "side",
            "BUY"
        )

        # -------------------------------------------------
        # Symbol
        # -------------------------------------------------

        if not symbol:

            errors.append(
                "MISSING_SYMBOL"
            )

        # -------------------------------------------------
        # Side
        # -------------------------------------------------

        if side != "BUY":

            errors.append(
                "INVALID_SIDE"
            )

        # -------------------------------------------------
        # Quantity
        # -------------------------------------------------

        try:

            quantity = int(
                quantity
            )

            if quantity <= 0:

                errors.append(
                    "INVALID_QUANTITY"
                )

        except Exception:

            errors.append(
                "INVALID_QUANTITY"
            )

        # -------------------------------------------------
        # Price
        # -------------------------------------------------

        try:

            price = float(
                price
            )

            if price <= 0:

                errors.append(
                    "INVALID_PRICE"
                )

        except Exception:

            errors.append(
                "INVALID_PRICE"
            )

        # -------------------------------------------------
        # Order value
        # -------------------------------------------------

        try:

            order_value = float(
                order_value
            )

            if order_value <= 0:

                errors.append(
                    "INVALID_ORDER_VALUE"
                )

        except Exception:

            errors.append(
                "INVALID_ORDER_VALUE"
            )

        # -------------------------------------------------
        # Mathematical consistency
        # -------------------------------------------------

        try:

            calculated_value = (
                price * quantity
            )

            if abs(
                calculated_value
                - order_value
            ) > 0.01:

                errors.append(
                    "ORDER_VALUE_MISMATCH"
                )

        except Exception:

            errors.append(
                "ORDER_VALUE_CALCULATION_ERROR"
            )

        # -------------------------------------------------
        # Execution readiness
        # -------------------------------------------------

        if execution_status not in (
            "READY",
            "READY_WITH_WARNING"
        ):

            errors.append(
                "EXECUTION_NOT_READY"
            )

        # -------------------------------------------------
        # Broker safety
        # -------------------------------------------------

        if broker_execution is not False:

            errors.append(
                "BROKER_EXECUTION_ENABLED"
            )

        # -------------------------------------------------
        # Hard block
        # -------------------------------------------------

        if errors:

            result = {

                "symbol": symbol,

                "execution_control":
                    "BLOCKED",

                "execution_reason":
                    errors[0],

                "approved": False,

                "errors": errors

            }

            self.blocked_orders.append(
                result
            )

            return result

        # -------------------------------------------------
        # Warning order
        # -------------------------------------------------

        if execution_status == (
            "READY_WITH_WARNING"
        ):

            result = {

                "symbol": symbol,

                "execution_control":
                    "APPROVED_WITH_WARNING",

                "execution_reason":
                    "EXECUTION_WARNING",

                "approved": True,

                "warning": True,

                "errors": []

            }

            self.warning_orders.append(
                result
            )

            return result

        # -------------------------------------------------
        # Fully approved
        # -------------------------------------------------

        result = {

            "symbol": symbol,

            "execution_control":
                "APPROVED",

            "execution_reason":
                "FINAL_EXECUTION_CHECKS_PASSED",

            "approved": True,

            "warning": False,

            "errors": []

        }

        self.approved_orders.append(
            result
        )

        return result

    # -------------------------------------------------
    # Control multiple orders
    # -------------------------------------------------

    def control_orders(self, orders):

        self.approved_orders = []
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
                self.control(
                    order
                )
            )

        return results

    # -------------------------------------------------
    # Approved orders
    # -------------------------------------------------

    def get_approved_orders(self):

        return list(
            self.approved_orders
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

            "approved":
                len(
                    self.approved_orders
                ),

            "approved_with_warning":
                len(
                    self.warning_orders
                ),

            "blocked":
                len(
                    self.blocked_orders
                ),

            "total":
                (
                    len(self.approved_orders)
                    +
                    len(self.warning_orders)
                    +
                    len(self.blocked_orders)
                ),

            "broker_execution":
                False

        }