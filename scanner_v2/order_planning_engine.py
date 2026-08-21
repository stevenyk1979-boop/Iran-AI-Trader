"""
Iran AI Trader Professional

Scanner V2

Sprint45-04

Order Planning Engine

Converts portfolio allocation results
into executable order plans.

IMPORTANT:
This engine DOES NOT send orders
to any broker.
"""


class OrderPlanningEngine:

    def __init__(
        self,
        lot_size=1
    ):

        self.lot_size = max(
            1,
            int(lot_size)
        )

        self.orders = []


    # -------------------------------------------------
    # Calculate share quantity
    # -------------------------------------------------

    def calculate_quantity(
        self,
        capital,
        price
    ):

        try:

            capital = float(capital)
            price = float(price)

            if capital <= 0:
                return 0

            if price <= 0:
                return 0

            quantity = int(
                capital / price
            )

            quantity = (
                quantity // self.lot_size
            ) * self.lot_size

            return quantity

        except Exception:

            return 0


    # -------------------------------------------------
    # Build one order
    # -------------------------------------------------

    def build_order(
        self,
        item
    ):

        if not isinstance(
            item,
            dict
        ):

            return None

        symbol = item.get(
            "symbol"
        )

        signal = item.get(
            "signal",
            "IGNORE"
        )

        capital = item.get(
            "capital",
            item.get(
                "allocated_capital",
                0
            )
        )

        price = item.get(
            "price",
            item.get(
                "reference_price",
                0
            )
        )

        allocation = item.get(
            "allocation_percent",
            item.get(
                "allocation",
                0
            )
        )

        if not symbol:

            return None

        if signal not in (
            "BUY",
            "STRONG BUY"
        ):

            return None

        quantity = self.calculate_quantity(
            capital,
            price
        )

        if quantity <= 0:

            return None

        order_value = (
            quantity * float(price)
        )

        return {

            "symbol": symbol,

            "side": "BUY",

            "signal": signal,

            "price": float(price),

            "capital": float(capital),

            "allocation_percent": float(
                allocation
            ),

            "quantity": quantity,

            "order_value": round(
                order_value,
                2
            ),

            "status": "READY",

            "broker_execution": False
        }


    # -------------------------------------------------
    # Build all orders
    # -------------------------------------------------

    def build_orders(
        self,
        portfolio
    ):

        self.orders = []

        if portfolio is None:
            return []

        if not isinstance(
            portfolio,
            list
        ):

            return []

        for item in portfolio:

            order = self.build_order(
                item
            )

            if order is not None:

                self.orders.append(
                    order
                )

        return self.orders


    # -------------------------------------------------
    # Get orders
    # -------------------------------------------------

    def get_orders(self):

        return list(
            self.orders
        )


    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(self):

        total_value = sum(
            order.get(
                "order_value",
                0
            )
            for order in self.orders
        )

        return {

            "orders": len(
                self.orders
            ),

            "total_order_value": round(
                total_value,
                2
            ),

            "symbols": [
                order.get(
                    "symbol"
                )
                for order in self.orders
            ],

            "broker_execution": False
        }