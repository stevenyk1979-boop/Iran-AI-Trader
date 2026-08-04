"""
Iran AI Trader Professional
Portfolio Risk Engine
Sprint33-D
"""


import statistics


from portfolio_risk_config import (

    MAX_ACCEPTABLE_DRAWDOWN,

    CRITICAL_DRAWDOWN,

    LOW_RISK_SCORE,

    MEDIUM_RISK_SCORE

)



class PortfolioRiskEngine:


    def __init__(self):

        pass



    # -------------------------------------

    def calculate_drawdown(

        self,

        prices

    ):

        """
        Calculate maximum drawdown
        """


        if not prices:

            return 0



        peak = max(prices)


        current = prices[-1]



        drawdown = (

            (peak - current)

            /

            peak

        ) * 100



        return round(

            drawdown,

            2

        )



    # -------------------------------------

    def calculate_volatility(

        self,

        prices

    ):

        """
        Simple volatility calculation
        """


        if len(prices) < 2:

            return 0



        returns = []


        for i in range(

            1,

            len(prices)

        ):


            change = (

                prices[i]

                -

                prices[i-1]

            ) / prices[i-1]



            returns.append(

                change

            )



        if len(returns) < 2:

            return 0



        volatility = statistics.stdev(

            returns

        ) * 100



        return round(

            volatility,

            2

        )



    # -------------------------------------

    def calculate_risk_score(

        self,

        drawdown,

        volatility

    ):

        """
        Risk score
        Higher is safer
        """


        score = 100



        score -= drawdown * 2


        score -= volatility * 5



        if score < 0:

            score = 0



        return round(

            score,

            2

        )



    # -------------------------------------

    def risk_level(

        self,

        score

    ):


        if score >= LOW_RISK_SCORE:

            return "LOW"


        elif score >= MEDIUM_RISK_SCORE:

            return "MEDIUM"



        else:

            return "HIGH"



    # -------------------------------------

    def analyze(

        self,

        prices

    ):

        """
        Full portfolio risk analysis
        """


        drawdown = self.calculate_drawdown(

            prices

        )


        volatility = self.calculate_volatility(

            prices

        )


        score = self.calculate_risk_score(

            drawdown,

            volatility

        )


        level = self.risk_level(

            score

        )



        action = "NORMAL"



        if drawdown >= CRITICAL_DRAWDOWN:

            action = "REDUCE POSITION"



        elif drawdown >= MAX_ACCEPTABLE_DRAWDOWN:

            action = "CAUTION"



        return {


            "drawdown": drawdown,


            "volatility": volatility,


            "risk_score": score,


            "risk_level": level,


            "action": action

        }