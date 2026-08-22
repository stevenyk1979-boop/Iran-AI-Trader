"""
Iran AI Trader Professional

Scanner V2

Sprint46

Portfolio Monitoring Engine

Monitors open positions and calculates:
- current P/L
- P/L percentage
- exposure
- risk status
- stop loss distance
- take profit distance
- portfolio summary

IMPORTANT:
This engine DOES NOT execute orders.
"""

class PortfolioMonitoringEngine:

    def __init__(self):
        self.monitored_positions = []

    # -------------------------------------------------
    # Safe numeric conversion
    # -------------------------------------------------

    def _number(self, value, default=0.0):

        try:
            return float(value)

        except Exception:
            return float(default)

    # -------------------------------------------------
    # Monitor one position
    # -------------------------------------------------

    def monitor_position(
        self,
        position,
        current_price
    ):

        if not isinstance(position, dict):
            return None

        symbol = position.get("symbol")

        if not symbol:
            return None

        entry_price = self._number(
            position.get("entry_price", 0)
        )

        quantity = int(
            self._number(
                position.get("quantity", 0)
            )
        )

        price = self._number(
            current_price
        )

        if entry_price <= 0:
            return None

        if quantity <= 0:
            return None

        if price <= 0:
            return None

        invested_value = (
            entry_price * quantity
        )

        current_value = (
            price * quantity
        )

        pnl = (
            current_value
            - invested_value
        )

        pnl_percent = (
            pnl / invested_value
        ) * 100

        stop_loss = self._number(
            position.get("stop_loss", 0)
        )

        take_profit = self._number(
            position.get("take_profit", 0)
        )

        if stop_loss > 0:

            stop_distance = (
                (price - stop_loss)
                / price
            ) * 100

        else:

            stop_distance = 0.0

        if take_profit > 0:

            target_distance = (
                (take_profit - price)
                / price
            ) * 100

        else:

            target_distance = 0.0

        status = position.get(
            "status",
            "OPEN"
        )

        monitored = dict(position)

        monitored.update({

            "current_price": round(
                price,
                2
            ),

            "invested_value": round(
                invested_value,
                2
            ),

            "current_value": round(
                current_value,
                2
            ),

            "pnl": round(
                pnl,
                2
            ),

            "pnl_percent": round(
                pnl_percent,
                2
            ),

            "stop_distance_percent": round(
                stop_distance,
                2
            ),

            "target_distance_percent": round(
                target_distance,
                2
            ),

            "status": status

        })

        return monitored

    # -------------------------------------------------
    # Monitor portfolio
    # -------------------------------------------------

    def monitor(
        self,
        positions,
        prices
    ):

        self.monitored_positions = []

        if not isinstance(
            positions,
            list
        ):

            return []

        if not isinstance(
            prices,
            dict
        ):

            return []

        for position in positions:

            if not isinstance(
                position,
                dict
            ):
                continue

            symbol = position.get(
                "symbol"
            )

            if symbol not in prices:
                continue

            result = self.monitor_position(
                position,
                prices[symbol]
            )

            if result is not None:

                self.monitored_positions.append(
                    result
                )

        return list(
            self.monitored_positions
        )

    # -------------------------------------------------
    # Open positions
    # -------------------------------------------------

    def get_open_positions(self):

        return [

            position

            for position in self.monitored_positions

            if position.get(
                "status"
            ) == "OPEN"

        ]

    # -------------------------------------------------
    # Profitable positions
    # -------------------------------------------------

    def get_profitable_positions(self):

        return [

            position

            for position in self.monitored_positions

            if position.get(
                "pnl",
                0
            ) > 0

        ]

    # -------------------------------------------------
    # Losing positions
    # -------------------------------------------------

    def get_losing_positions(self):

        return [

            position

            for position in self.monitored_positions

            if position.get(
                "pnl",
                0
            ) < 0

        ]

    # -------------------------------------------------
    # Portfolio P/L
    # -------------------------------------------------

    def total_pnl(self):

        return round(

            sum(
                position.get(
                    "pnl",
                    0
                )
                for position
                in self.monitored_positions
            ),

            2
        )

    # -------------------------------------------------
    # Invested value
    # -------------------------------------------------

    def total_invested(self):

        return round(

            sum(
                position.get(
                    "invested_value",
                    0
                )
                for position
                in self.monitored_positions
            ),

            2
        )

    # -------------------------------------------------
    # Current value
    # -------------------------------------------------

    def total_current_value(self):

        return round(

            sum(
                position.get(
                    "current_value",
                    0
                )
                for position
                in self.monitored_positions
            ),

            2
        )

    # -------------------------------------------------
    # Portfolio P/L percentage
    # -------------------------------------------------

    def total_pnl_percent(self):

        invested = self.total_invested()

        if invested <= 0:
            return 0.0

        return round(

            (
                self.total_pnl()
                / invested
            ) * 100,

            2
        )

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(self):

        total = len(
            self.monitored_positions
        )

        open_count = len(
            self.get_open_positions()
        )

        profitable = len(
            self.get_profitable_positions()
        )

        losing = len(
            self.get_losing_positions()
        )

        return {

            "total_positions": total,

            "open_positions": open_count,

            "profitable_positions":
                profitable,

            "losing_positions":
                losing,

            "invested_value":
                self.total_invested(),

            "current_value":
                self.total_current_value(),

            "total_pnl":
                self.total_pnl(),

            "total_pnl_percent":
                self.total_pnl_percent()

        }