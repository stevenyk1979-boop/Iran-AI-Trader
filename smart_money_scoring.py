"""
Iran AI Trader Professional
Smart Money Scoring Engine
Sprint31-C
"""


class SmartMoneyScoring:


    def __init__(self):

        # وزن پول هوشمند در امتیاز نهایی

        self.weight = 0.30



    # -------------------------------------

    def calculate(

        self,

        technical_score,

        smart_money_score

    ):

        """
        Combine technical and smart money score
        """


        final_score = (

            technical_score * (1 - self.weight)

            +

            smart_money_score * self.weight

        )


        return round(

            final_score,

            2

        )



    # -------------------------------------

    def status(

        self,

        smart_money_score

    ):


        if smart_money_score >= 75:


            return "ACCUMULATION"



        elif smart_money_score >= 50:


            return "WATCH"



        else:


            return "WEAK"