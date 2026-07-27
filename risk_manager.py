"""
Iran AI Trader V2.0 Alpha
Risk Manager
"""


class RiskManager:

    def __init__(self):

        self.max_position_size = 0.20

        self.stop_loss = 0.03

        self.take_profit = 0.08

    def position_size(self, capital):

        """
        حداکثر سرمایه مجاز برای هر معامله
        """

        return round(capital * self.max_position_size, 2)

    def stop_loss_price(self, entry_price):

        return round(
            entry_price * (1 - self.stop_loss),
            2
        )

    def take_profit_price(self, entry_price):

        return round(
            entry_price * (1 + self.take_profit),
            2
        )