"""
Iran AI Trader V2.0 Alpha
Position Manager
"""


class PositionManager:

    def __init__(self):

        self.positions = []

    def open_position(self, symbol, quantity, entry_price):

        self.positions.append({

            "symbol": symbol,

            "quantity": quantity,

            "entry": entry_price

        })

    def count(self):

        return len(self.positions)

    def list_positions(self):

        return self.positions