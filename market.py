"""
Iran AI Trader V2.0
Market Module
"""

from datetime import datetime


class MarketManager:

    def __init__(self):
        self.market_name = "Iran Stock Market"

    def status(self):
        print(f"Market : {self.market_name}")
        print(f"Time   : {datetime.now()}")

    def update(self):
        print("Market update module is ready.")