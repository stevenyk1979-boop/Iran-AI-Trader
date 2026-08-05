"""
Iran AI Trader Professional
Macro Engine
Sprint36.5
"""


class MacroEngine:


    def __init__(self):

        pass


    # -------------------------------------

    def index_score(

        self,

        index_change

    ):


        if index_change >= 2:

            return 40


        elif index_change >= 1:

            return 30


        elif index_change >= 0:

            return 20


        elif index_change >= -1:

            return 10


        return 0


    # -------------------------------------

    def equal_weight_score(

        self,

        equal_change

    ):


        if equal_change >= 2:

            return 30


        elif equal_change >= 1:

            return 20


        elif equal_change >= 0:

            return 10


        return 0


    # -------------------------------------

    def money_flow_score(

        self,

        money_flow

    ):


        if money_flow >= 80:

            return 30


        elif money_flow >= 60:

            return 20


        elif money_flow >= 40:

            return 10


        return 0


    # -------------------------------------

    def calculate(

        self,

        index_change,

        equal_change,

        money_flow

    ):


        score = 0


        score += self.index_score(

            index_change

        )


        score += self.equal_weight_score(

            equal_change

        )


        score += self.money_flow_score(

            money_flow

        )


        if score > 100:

            score = 100


        return score