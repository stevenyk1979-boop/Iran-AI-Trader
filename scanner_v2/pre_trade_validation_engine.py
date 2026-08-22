"""
Iran AI Trader Professional

Scanner V2

Sprint45-05

Pre-Trade Validation Engine

Validates planned orders before any future broker execution.

IMPORTANT:
This engine DOES NOT execute orders.
It only validates them.
"""


class PreTradeValidationEngine:

    VALID_SIGNALS = {
        "BUY",
        "STRONG BUY"
    }

    def __init__(
        self,
        max_order_value=None,
        max_orders=None
    ):

        self.max_order_value = (
            None
            if max_order_value is None
            else float(max_order_value)
        )

        self.max_orders = (
            None
            if max_orders is None
            else int(max_orders)
        )

        self.valid_orders = []
        self.rejected_orders = []

    # -------------------------------------------------
    # Validate one order
    # -------------------------------------------------

    def validate_order(self, order):

        errors = []

        if not isinstance(order, dict):

            return {
                "valid": False,
                "errors": [
                    "ORDER_NOT_DICT"
                ]
            }

        symbol = order.get(
            "symbol"
        )

        signal = order.get(
            "signal"
        )

        price = order.get(
            "price"
        )

        capital = order.get(
            "capital"
        )

        quantity = order.get(
            "quantity"
        )

        order_value = order.get(
            "order_value"
        )

        status = order.get(
            "status"
        )

        broker_execution = order.get(
            "broker_execution",
            False
        )

        # -------------------------------------------------
        # Symbol
        # -------------------------------------------------

        if not symbol:

            errors.append(
                "MISSING_SYMBOL"
            )

        # -------------------------------------------------
        # Signal
        # -------------------------------------------------

        if signal not in self.VALID_SIGNALS:

            errors.append(
                "INVALID_SIGNAL"
            )

        # -------------------------------------------------
        # Price
        # -------------------------------------------------

        try:

            price = float(price)

            if price <= 0:

                errors.append(
                    "INVALID_PRICE"
                )

        except Exception:

            errors.append(
                "INVALID_PRICE"
            )

        # -------------------------------------------------
        # Capital
        # -------------------------------------------------

        try:

            capital = float(capital)

            if capital <= 0:

                errors.append(
                    "INVALID_CAPITAL"
                )

        except Exception:

            errors.append(
                "INVALID_CAPITAL"
            )

        # -------------------------------------------------
        # Quantity
        # -------------------------------------------------

        try:

            quantity = int(quantity)

            if quantity <= 0:

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
        # Capital consistency
        # -------------------------------------------------

        try:

            if order_value > capital:

                errors.append(
                    "ORDER_EXCEEDS_CAPITAL"
                )

        except Exception:

            errors.append(
                "CAPITAL_VALIDATION_ERROR"
            )

        # -------------------------------------------------
        # Status
        # -------------------------------------------------

        if status != "READY":

            errors.append(
                "ORDER_NOT_READY"
            )

        # -------------------------------------------------
        # Broker safety
        # -------------------------------------------------

        if broker_execution is not False:

            errors.append(
                "BROKER_EXECUTION_ENABLED"
            )

        return {

            "valid": len(
                errors
            ) == 0,

            "errors": errors,

            "symbol": symbol
        }

    # -------------------------------------------------
    # Validate order list
    # -------------------------------------------------

    def validate_orders(self, orders):

        self.valid_orders = []
        self.rejected_orders = []

        if orders is None:

            return []

        if not isinstance(
            orders,
            list
        ):

            return []

        # -------------------------------------------------
        # Maximum order count
        # -------------------------------------------------

        if (
            self.max_orders is not None
            and len(orders)
            > self.max_orders
        ):

            orders = orders[
                :self.max_orders
            ]

        total_value = 0.0

        # -------------------------------------------------
        # Validate each order
        # -------------------------------------------------

        for order in orders:

            result = self.validate_order(
                order
            )

            if not result["valid"]:

                rejected = dict(
                    order
                )

                rejected[
                    "validation_status"
                ] = "REJECTED"

                rejected[
                    "validation_errors"
                ] = result[
                    "errors"
                ]

                self.rejected_orders.append(
                    rejected
                )

                continue

            try:

                value = float(
                    order[
                        "order_value"
                    ]
                )

            except Exception:

                value = 0.0

            # -------------------------------------------------
            # Maximum total order value
            # -------------------------------------------------

            if (
                self.max_order_value
                is not None
                and
                total_value + value
                > self.max_order_value
            ):

                rejected = dict(
                    order
                )

                rejected[
                    "validation_status"
                ] = "REJECTED"

                rejected[
                    "validation_errors"
                ] = [
                    "MAX_ORDER_VALUE_EXCEEDED"
                ]

                self.rejected_orders.append(
                    rejected
                )

                continue

            validated = dict(
                order
            )

            validated[
                "validation_status"
            ] = "READY"

            validated[
                "validation_errors"
            ] = []

            self.valid_orders.append(
                validated
            )

            total_value += value

        return list(
            self.valid_orders
        )

    # -------------------------------------------------
    # Get valid orders
    # -------------------------------------------------

    def get_valid_orders(self):

        return list(
            self.valid_orders
        )

    # -------------------------------------------------
    # Get rejected orders
    # -------------------------------------------------

    def get_rejected_orders(self):

        return list(
            self.rejected_orders
        )

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(self):

        total_valid_value = round(
            sum(
                float(
                    order.get(
                        "order_value",
                        0
                    )
                )
                for order in self.valid_orders
            ),
            2
        )

        return {

            "valid_orders": len(
                self.valid_orders
            ),

            "rejected_orders": len(
                self.rejected_orders
            ),

            "total_valid_order_value":
                total_valid_value,

            "broker_execution":
                False
        }