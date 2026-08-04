"""
Iran AI Trader Professional
Portfolio Brain
Sprint34
"""


from portfolio_brain_config import (

    MIN_FINAL_SCORE,

    MIN_SMART_MONEY_SCORE,

    TECHNICAL_WEIGHT,

    SMART_MONEY_WEIGHT,

    PORTFOLIO_WEIGHT,

    RISK_WEIGHT

)



class PortfolioBrain:


    def __init__(self):

        pass



    # -------------------------------------

    def calculate_final_score(

        self,

        technical_score,

        smart_money_score,

        portfolio_score,

        risk_score

    ):

        """

        Combine all intelligence engines

        """


        score = (

            technical_score

            *

            TECHNICAL_WEIGHT

            +

            smart_money_score

            *

            SMART_MONEY_WEIGHT

            +

            portfolio_score

            *

            PORTFOLIO_WEIGHT

            +

            risk_score

            *

            RISK_WEIGHT

        )


        return round(

            score,

            2

        )



    # -------------------------------------

    def decision(

        self,

        final_score,

        smart_money_score

    ):

        """

        Final AI decision

        """


        if (

            final_score >= MIN_FINAL_SCORE

            and

            smart_money_score >= MIN_SMART_MONEY_SCORE

        ):


            return "APPROVED BUY"



        elif final_score >= 60:


            return "WATCH"



        else:


            return "REJECT"



    # -------------------------------------

    def analyze(

        self,

        data

    ):

        """

        Full portfolio brain analysis

        """


        technical_score = data.get(

            "technical_score",

            0

        )


        smart_money_score = data.get(

            "smart_money_score",

            0

        )


        portfolio_score = data.get(

            "portfolio_score",

            0

        )


        risk_score = data.get(

            "risk_score",

            0

        )



        final_score = self.calculate_final_score(

            technical_score,

            smart_money_score,

            portfolio_score,

            risk_score

        )



        result = {


            "symbol": data.get(

                "symbol"

            ),


            "technical_score": technical_score,


            "smart_money_score": smart_money_score,


            "portfolio_score": portfolio_score,


            "risk_score": risk_score,


            "final_ai_score": final_score,


            "decision": self.decision(

                final_score,

                smart_money_score

            )

        }


        return result