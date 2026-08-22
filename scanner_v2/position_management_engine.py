"""
Iran AI Trader Professional

Scanner V2

Sprint45-04

Position Management Engine

Manages an approved trade after entry.

No broker connection.
No real order execution.
"""


class PositionManagementEngine:

    def __init__(self):

        self.positions = []

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
    # Build position
    # -------------------------------------------------

    def build_position(
        self,
        trade_plan
    ):

        if not isinstance(
            trade_plan,
            dict
        ):

            return None

        if trade_plan.get(
            "final_status"
        ) != "READY":

            return None

        symbol = trade_plan.get(
            "symbol"
        )

        if symbol is None:

            return None

        entry_price = self._number(
            trade_plan.get(
                "entry_price",
                0
            )
        )

        quantity = int(
            self._number(
                trade_plan.get(
                    "quantity",
                    0
                )
            )
        )

        risk_reward = self._number(
            trade_plan.get(
                "risk_reward",
                0
            )
        )

        if entry_price <= 0:

            return None

        if quantity <= 0:

            return None

        # Default risk model:
        # risk = 1 / (1 + R/R)

        if risk_reward > 0:

            risk_percent = (
                1 / (
                    1 + risk_reward
                )
            ) * 100

        else:

            risk_percent = 0

        stop_loss = (
            entry_price
            * (
                1
                - risk_percent / 100
            )
        )

        take_profit = (
            entry_price
            + (
                entry_price
                - stop_loss
            ) * risk_reward
        )

        position = {

            "symbol": symbol,

            "entry_price": round(
                entry_price,
                2
            ),

            "quantity": quantity,

            "risk_reward": round(
                risk_reward,
                2
            ),

            "risk_percent": round(
                risk_percent,
                2
            ),

            "stop_loss": round(
                stop_loss,
                2
            ),

            "take_profit": round(
                take_profit,
                2
            ),

            "current_price": round(
                entry_price,
                2
            ),

            "status": "OPEN",

            "exit_reason": None

        }

        return position

    # -------------------------------------------------
    # Update current price
    # -------------------------------------------------

    def update_price(
        self,
        position,
        current_price
    ):

        if not isinstance(
            position,
            dict
        ):

            return None

        price = self._number(
            current_price
        )

        if price <= 0:

            return position

        position[
            "current_price"
        ] = round(
            price,
            2
        )

        stop_loss = self._number(
            position.get(
                "stop_loss"
            )
        )

        take_profit = self._number(
            position.get(
                "take_profit"
            )
        )

        if price <= stop_loss:

            position[
                "status"
            ] = "CLOSED"

            position[
                "exit_reason"
            ] = "STOP LOSS"

        elif price >= take_profit:

            position[
                "status"
            ] = "CLOSED"

            position[
                "exit_reason"
            ] = "TAKE PROFIT"

        return position

    # -------------------------------------------------
    # Build multiple positions
    # -------------------------------------------------

    def build(
        self,
        trade_plans
    ):

        self.positions = []

        if not isinstance(
            trade_plans,
            list
        ):

            return []

        for plan in trade_plans:

            position = self.build_position(
                plan
            )

            if position is not None:

                self.positions.append(
                    position
                )

        return list(
            self.positions
        )

    # -------------------------------------------------
    # Get open positions
    # -------------------------------------------------

    def get_open_positions(self):

        return [

            position

            for position in self.positions

            if position.get(
                "status"
            ) == "OPEN"

        ]

    # -------------------------------------------------
    # Get closed positions
    # -------------------------------------------------

    def get_closed_positions(self):

        return [

            position

            for position in self.positions

            if position.get(
                "status"
            ) == "CLOSED"

        ]

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(self):

        return {

            "total_positions": len(
                self.positions
            ),

            "open": len(
                self.get_open_positions()
            ),

            "closed": len(
                self.get_closed_positions()
            )

        }