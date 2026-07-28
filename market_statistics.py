"""
Iran AI Trader V2.0 Alpha
Market Statistics
"""


class MarketStatistics:

    def best(self, ranking):

        return max(ranking, key=lambda x: x["score"])

    def worst(self, ranking):

        return min(ranking, key=lambda x: x["score"])

    def average_score(self, ranking):

        if not ranking:
            return 0

        total = sum(item["score"] for item in ranking)

        return round(total / len(ranking), 2)