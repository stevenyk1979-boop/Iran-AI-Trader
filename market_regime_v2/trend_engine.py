"""
Iran AI Trader Professional
Trend Engine
Sprint36.5
"""


class TrendEngine:


    def __init__(self):

        pass


    # -------------------------------------

    def ema_score(

        self,

        ema20,

        ema50,

        ema100

    ):

        """
        EMA Trend Alignment
        """


        score = 0


        if ema20 > ema50:

            score += 30


        if ema50 > ema100:

            score += 30


        if ema20 > ema100:

            score += 20


        return score


    # -------------------------------------

    def price_score(

        self,

        price,

        ema20,

        ema50

    ):


        score = 0


        if price > ema20:

            score += 10


        if price > ema50:

            score += 10


        return score


    # -------------------------------------

    def slope_score(

        self,

        ema50,

        ema50_prev

    ):


        if ema50 > ema50_prev:

            return 20


        return 0


    # -------------------------------------

    def calculate(

        self,

        price,

        ema20,

        ema50,

        ema100,

        ema50_prev

    ):


        score = 0


        score += self.ema_score(

            ema20,

            ema50,

            ema100

        )


        score += self.price_score(

            price,

            ema20,

            ema50

        )


        score += self.slope_score(

            ema50,

            ema50_prev

        )


        if score > 100:

            score = 100


        return score