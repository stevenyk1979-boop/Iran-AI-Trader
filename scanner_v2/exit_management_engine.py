"""
Iran AI Trader Professional

Scanner V2

Sprint45-06

Exit Management Engine

Centralized exit decision engine.

Checks:
    - Take Profit
    - Stop Loss
    - Trailing Stop
"""


class ExitManagementEngine:

    def __init__(self):

        self.closed_positions = []

    # -------------------------------------------------
    # Evaluate one position
    # -------------------------------------------------

    def evaluate(self, position, current_price):

        if not isinstance(position, dict):

            return {
                "status": "REJECTED",
                "exit_reason": "INVALID POSITION"
            }

        try:

            price = float(current_price)

        except Exception:

            return {
                **position,
                "status": "REJECTED",
                "exit_reason": "INVALID PRICE"
            }

        status = position.get(
            "status",
            "OPEN"
        )

        if status == "CLOSED":

            return dict(position)

        take_profit = position.get(
            "take_profit"
        )

        stop_loss = position.get(
            "stop_loss"
        )

        trailing_stop = position.get(
            "trailing_stop"
        )

        # -------------------------------------------------
        # Take Profit
        # -------------------------------------------------

        if (
            take_profit is not None
            and price >= float(take_profit)
        ):

            return self._close_position(
                position,
                price,
                "TAKE PROFIT"
            )

        # -------------------------------------------------
        # Stop Loss
        # -------------------------------------------------

        if (
            stop_loss is not None
            and price <= float(stop_loss)
        ):

            return self._close_position(
                position,
                price,
                "STOP LOSS"
            )

        # -------------------------------------------------
        # Trailing Stop
        # -------------------------------------------------

        if (
            trailing_stop is not None
            and price <= float(trailing_stop)
        ):

            return self._close_position(
                position,
                price,
                "TRAILING STOP"
            )

        # -------------------------------------------------
        # Still open
        # -------------------------------------------------

        result = dict(position)

        result["status"] = "OPEN"

        result["current_price"] = price

        return result

    # -------------------------------------------------
    # Close position
    # -------------------------------------------------

    def _close_position(
        self,
        position,
        price,
        reason
    ):

        result = dict(position)

        result["status"] = "CLOSED"

        result["current_price"] = price

        result["exit_reason"] = reason

        self.closed_positions.append(
            dict(result)
        )

        return result

    # -------------------------------------------------
    # Batch evaluation
    # -------------------------------------------------

    def evaluate_all(
        self,
        positions
    ):

        if positions is None:

            return []

        results = []

        for position in positions:

            current_price = position.get(
                "current_price"
            )

            if current_price is None:

                results.append(
                    {
                        **position,
                        "status": "REJECTED",
                        "exit_reason": "NO CURRENT PRICE"
                    }
                )

                continue

            results.append(
                self.evaluate(
                    position,
                    current_price
                )
            )

        return results

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(self):

        return {
            "closed_count": len(
                self.closed_positions
            ),

            "exit_reasons": [
                item.get(
                    "exit_reason"
                )
                for item in self.closed_positions
            ]
        }