"""
Iran AI Trader Professional
Breadth Engine
Sprint36.5
"""


class BreadthEngine:

    def __init__(self):
        pass

    # -------------------------------------

    def positive_score(
        self,
        positive,
        negative,
        unchanged
    ):

        total = positive + negative + unchanged

        if total == 0:
            return 0

        ratio = positive / total

        if ratio >= 0.80:
            return 50

        elif ratio >= 0.70:
            return 40

        elif ratio >= 0.60:
            return 30

        elif ratio >= 0.50:
            return 20

        elif ratio >= 0.40:
            return 10

        return 0

    # -------------------------------------

    def advance_decline_score(
        self,
        positive,
        negative
    ):

        if negative == 0:
            return 50

        ratio = positive / negative

        if ratio >= 3:
            return 50

        elif ratio >= 2:
            return 40

        elif ratio >= 1.5:
            return 30

        elif ratio >= 1:
            return 20

        return 0

    # -------------------------------------

    def calculate(
        self,
        positive,
        negative,
        unchanged
    ):

        score = 0

        score += self.positive_score(
            positive,
            negative,
            unchanged
        )

        score += self.advance_decline_score(
            positive,
            negative
        )

        if score > 100:
            score = 100

        return score