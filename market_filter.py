"""
Iran AI Trader V2.0 Alpha
Market Filter
"""


class MarketFilter:

    def filter(self, ranking, minimum_score=10):

        result = []

        for row in ranking:

            if row["score"] >= minimum_score:

                result.append(row)

        return result