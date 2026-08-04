"""
Iran AI Trader Professional
Capital Manager
Sprint32-A
"""


class CapitalManager:

    def __init__(

        self,

        capital=100_000_000,

        risk_percent=1

    ):

        self.capital = capital

        self.risk_percent = risk_percent

    # -----------------------------------

    def max_risk_amount(self):

        """
        Maximum money allowed
        to lose in one trade
        """

        return (

            self.capital

            * self.risk_percent

            / 100

        )

    # -----------------------------------

    def allocate(

        self,

        candidate

    ):

        """
        Allocate capital
        according to AI score
        """

        score = candidate.get(

            "final_score",

            candidate.get(

                "score",

                0

            )

        )

        if score >= 95:

            allocation = 0.10

        elif score >= 90:

            allocation = 0.08

        elif score >= 80:

            allocation = 0.06

        elif score >= 70:

            allocation = 0.04

        else:

            allocation = 0.00

        capital = (

            self.capital

            * allocation

        )

        return {

            "allocation_percent": allocation * 100,

            "capital": round(capital)

        }