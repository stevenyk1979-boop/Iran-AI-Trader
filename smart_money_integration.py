"""
Iran AI Trader Professional
Smart Money Integration
Sprint31-D
"""

from smart_money_adapter import SmartMoneyAdapter
from smart_money_scoring import SmartMoneyScoring


class SmartMoneyIntegration:


    def __init__(self):

        self.adapter = SmartMoneyAdapter()

        self.scoring = SmartMoneyScoring()


    # ----------------------------------------

    def integrate(self, item):


        item = self.adapter.apply(

            item

        )


        final_score = self.scoring.calculate(

            item["score"],

            item["smart_money_score"]

        )


        item["technical_score"] = item["score"]

        item["final_score"] = final_score


        return item