"""
Iran AI Trader Professional

Scanner V2

Sprint46

Trade Journal & Performance Engine

Records closed trades and calculates
basic trading performance statistics.

IMPORTANT:
No broker connection.
No real order execution.
"""


class TradeJournalEngine:

    def __init__(self):

        self.trades = []

    # -------------------------------------------------
    # Safe number
    # -------------------------------------------------

    def _number(self, value, default=0.0):

        try:
            return float(value)

        except Exception:
            return float(default)

    # -------------------------------------------------
    # Record trade
    # -------------------------------------------------

    def record_trade(self, position):

        if not isinstance(position, dict):
            return None

        if position.get("status") != "CLOSED":
            return None

        symbol = position.get("symbol")

        if not symbol:
            return None

        entry_price = self._number(
            position.get("entry_price")
        )

        exit_price = self._number(
            position.get(
                "exit_price",
                position.get(
                    "current_price"
                )
            )
        )

        quantity = int(
            self._number(
                position.get("quantity")
            )
        )

        if entry_price <= 0:
            return None

        if exit_price <= 0:
            return None

        if quantity <= 0:
            return None

        invested = (
            entry_price *
            quantity
        )

        current_value = (
            exit_price *
            quantity
        )

        pnl = (
            current_value -
            invested
        )

        pnl_percent = (
            pnl / invested
        ) * 100

        exit_reason = position.get(
            "exit_reason"
        )

        if exit_reason == "TAKE PROFIT":
            result = "WIN"

        elif exit_reason == "STOP LOSS":
            result = "LOSS"

        elif pnl > 0:
            result = "WIN"

        elif pnl < 0:
            result = "LOSS"

        else:
            result = "BREAKEVEN"

        trade = {

            "symbol": symbol,

            "entry_price": round(
                entry_price,
                2
            ),

            "exit_price": round(
                exit_price,
                2
            ),

            "quantity": quantity,

            "invested": round(
                invested,
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

            "exit_reason":
                exit_reason,

            "result":
                result,

            "status":
                "CLOSED"

        }

        self.trades.append(trade)

        return trade

    # -------------------------------------------------
    # Record multiple trades
    # -------------------------------------------------

    def record(self, positions):

        if not isinstance(
            positions,
            list
        ):
            return []

        for position in positions:

            self.record_trade(
                position
            )

        return list(
            self.trades
        )

    # -------------------------------------------------
    # Get trades
    # -------------------------------------------------

    def get_trades(self):

        return list(
            self.trades
        )

    # -------------------------------------------------
    # Winning trades
    # -------------------------------------------------

    def winning_trades(self):

        return [

            trade

            for trade in self.trades

            if trade.get(
                "result"
            ) == "WIN"

        ]

    # -------------------------------------------------
    # Losing trades
    # -------------------------------------------------

    def losing_trades(self):

        return [

            trade

            for trade in self.trades

            if trade.get(
                "result"
            ) == "LOSS"

        ]

    # -------------------------------------------------
    # Breakeven trades
    # -------------------------------------------------

    def breakeven_trades(self):

        return [

            trade

            for trade in self.trades

            if trade.get(
                "result"
            ) == "BREAKEVEN"

        ]

    # -------------------------------------------------
    # Total P/L
    # -------------------------------------------------

    def total_pnl(self):

        return round(
            sum(
                trade.get(
                    "pnl",
                    0
                )
                for trade in self.trades
            ),
            2
        )

    # -------------------------------------------------
    # Total invested
    # -------------------------------------------------

    def total_invested(self):

        return round(
            sum(
                trade.get(
                    "invested",
                    0
                )
                for trade in self.trades
            ),
            2
        )

    # -------------------------------------------------
    # Win rate
    # -------------------------------------------------

    def win_rate(self):

        total = len(
            self.trades
        )

        if total == 0:
            return 0.0

        wins = len(
            self.winning_trades()
        )

        return round(
            (
                wins /
                total
            ) * 100,
            2
        )

    # -------------------------------------------------
    # Average win
    # -------------------------------------------------

    def average_win(self):

        trades = (
            self.winning_trades()
        )

        if not trades:
            return 0.0

        return round(
            sum(
                trade["pnl"]
                for trade in trades
            ) / len(trades),
            2
        )

    # -------------------------------------------------
    # Average loss
    # -------------------------------------------------

    def average_loss(self):

        trades = (
            self.losing_trades()
        )

        if not trades:
            return 0.0

        return round(
            sum(
                trade["pnl"]
                for trade in trades
            ) / len(trades),
            2
        )

    # -------------------------------------------------
    # Total profit
    # -------------------------------------------------

    def total_profit(self):

        return round(
            sum(
                trade["pnl"]
                for trade in self.winning_trades()
            ),
            2
        )

    # -------------------------------------------------
    # Total loss
    # -------------------------------------------------

    def total_loss(self):

        return round(
            sum(
                trade["pnl"]
                for trade in self.losing_trades()
            ),
            2
        )

    # -------------------------------------------------
    # Profit factor
    # -------------------------------------------------

    def profit_factor(self):

        total_loss = abs(
            self.total_loss()
        )

        if total_loss == 0:

            if self.total_profit() > 0:
                return float("inf")

            return 0.0

        return round(
            self.total_profit() /
            total_loss,
            2
        )

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(self):

        return {

            "total_trades":
                len(self.trades),

            "winning_trades":
                len(
                    self.winning_trades()
                ),

            "losing_trades":
                len(
                    self.losing_trades()
                ),

            "breakeven_trades":
                len(
                    self.breakeven_trades()
                ),

            "win_rate_percent":
                self.win_rate(),

            "total_invested":
                self.total_invested(),

            "total_profit":
                self.total_profit(),

            "total_loss":
                self.total_loss(),

            "net_pnl":
                self.total_pnl(),

            "average_win":
                self.average_win(),

            "average_loss":
                self.average_loss(),

            "profit_factor":
                self.profit_factor()

        }