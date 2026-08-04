"""
Iran AI Trader Professional
Pipeline Brain Adapter
Sprint36-B
"""


class PipelineBrainAdapter:


    def __init__(self):

        pass



    # -------------------------------------

    def get_smart_money_score(

        self,

        candidate

    ):

        """
        Extract smart money score
        """


        return candidate.get(

            "smart_money_score",

            candidate.get(

                "money_flow_score",

                50

            )

        )



    # -------------------------------------

    def get_portfolio_score(

        self,

        candidate

    ):

        """
        Portfolio quality score
        """


        if "portfolio_score" in candidate:

            return candidate["portfolio_score"]



        score = candidate.get(

            "score",

            0

        )


        # normalize candidate quality

        if score >= 80:

            return 90


        elif score >= 60:

            return 70


        else:

            return 50



    # -------------------------------------

    def get_risk_score(

        self,

        candidate

    ):

        """
        Risk score
        Higher is safer
        """


        if "risk_score" in candidate:

            return candidate["risk_score"]



        risk = candidate.get(

            "risk",

            0

        )



        # convert risk value

        if risk <= 20:

            return 80


        elif risk <= 50:

            return 60


        else:

            return 40



    # -------------------------------------

    def adapt(

        self,

        candidate

    ):

        """
        Convert pipeline candidate
        to PortfolioBrain format
        """


        technical_score = candidate.get(

            "score",

            0

        )



        return {


            "symbol": candidate.get(

                "symbol"

            ),



            "technical_score": technical_score,



            "smart_money_score": self.get_smart_money_score(

                candidate

            ),



            "portfolio_score": self.get_portfolio_score(

                candidate

            ),



            "risk_score": self.get_risk_score(

                candidate

            )

        }