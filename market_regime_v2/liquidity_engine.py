"""
Iran AI Trader Professional
Liquidity Engine
Sprint36.5
"""


class LiquidityEngine:


    def __init__(self):

        pass



    # -------------------------------------

    def volume_score(

        self,

        volume,

        avg_volume

    ):

        """
        Compare today's volume
        with average volume
        """


        if avg_volume <= 0:

            return 0


        ratio = volume / avg_volume


        if ratio >= 2:

            return 40


        elif ratio >= 1.5:

            return 30


        elif ratio >= 1:

            return 20


        elif ratio >= 0.5:

            return 10


        return 0



    # -------------------------------------

    def value_score(

        self,

        value,

        avg_value

    ):

        """
        Compare trading value
        """


        if avg_value <= 0:

            return 0


        ratio = value / avg_value


        if ratio >= 2:

            return 40


        elif ratio >= 1.5:

            return 30


        elif ratio >= 1:

            return 20


        elif ratio >= 0.5:

            return 10


        return 0



    # -------------------------------------

    def money_flow_score(

        self,

        money_flow

    ):

        """
        Smart money flow
        """


        if money_flow >= 80:

            return 20


        elif money_flow >= 60:

            return 15


        elif money_flow >= 40:

            return 10


        return 0



    # -------------------------------------

    def calculate(

        self,

        volume,

        avg_volume,

        value,

        avg_value,

        money_flow

    ):

        """
        Final liquidity score
        """


        score = 0


        score += self.volume_score(

            volume,

            avg_volume

        )


        score += self.value_score(

            value,

            avg_value

        )


        score += self.money_flow_score(

            money_flow

        )


        if score > 100:

            score = 100


        return score