"""
Iran AI Trader Professional

Scanner V2

Sprint45-05

Trailing Stop Engine

Protects accumulated profit by moving the stop loss
upward as the market price increases.

No broker connection.
No real order execution.
"""


class TrailingStopEngine:

    def __init__(
        self,
        trailing_percent=5.0
    ):

        self.trailing_percent = float(
            trailing_percent
        )

        if self.trailing_percent <= 0:

            self.trailing_percent = 5.0

    # -------------------------------------------------
    # Calculate trailing stop
    # -------------------------------------------------

    def calculate_stop(
        self,
        current_price
    ):

        try:

            price = float(
                current_price
            )

            if price <= 0:

                return 0.0

            stop = (
                price
                * (
                    1
                    - self.trailing_percent / 100
                )
            )

            return round(
                stop,
                2
            )

        except Exception:

            return 0.0

    # -------------------------------------------------
    # Update position
    # -------------------------------------------------

    def update(
        self,
        position,
        current_price
    ):

        if not isinstance(
            position,
            dict
        ):

            return None

        if position.get(
            "status"
        ) != "OPEN":

            return position

        try:

            price = float(
                current_price
            )

        except Exception:

            return position

        if price <= 0:

            return position

        current_stop = float(
            position.get(
                "stop_loss",
                0
            )
        )

        trailing_stop = (
            self.calculate_stop(
                price
            )
        )

        # Stop loss must only move upward.
        if trailing_stop > current_stop:

            position[
                "stop_loss"
            ] = trailing_stop

        position[
            "current_price"
        ] = round(
            price,
            2
        )

        # Check whether price has hit stop.
        if price <= float(
            position.get(
                "stop_loss",
                0
            )
        ):

            position[
                "status"
            ] = "CLOSED"

            position[
                "exit_reason"
            ] = "TRAILING STOP"

        return position

    # -------------------------------------------------
    # Update multiple positions
    # -------------------------------------------------

    def update_positions(
        self,
        positions,
        prices
    ):

        if not isinstance(
            positions,
            list
        ):

            return []

        if not isinstance(
            prices,
            dict
        ):

            return positions

        for position in positions:

            symbol = position.get(
                "symbol"
            )

            if symbol not in prices:

                continue

            self.update(
                position,
                prices[symbol]
            )

        return positions