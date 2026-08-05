"""
Iran AI Trader Professional
Volatility Engine
Sprint36.5
"""


class VolatilityEngine:


    def __init__(self):

        pass


    # -------------------------------------

    def atr_score(

        self,

        atr_percent

    ):

        """
        ATR percent
        Lower volatility = higher score
        """


        if atr_percent <= 2:

            return 40


        elif atr_percent <= 3:

            return 30


        elif atr_percent <= 5:

            return 20


        elif atr_percent <= 7:

            return 10


        return 0


    # -------------------------------------

    def index_volatility_score(

        self,

        market_volatility

    ):

        """
        Market volatility
        """


        if market_volatility <= 1:

            return 40


        elif market_volatility <= 2:

            return 30


        elif market_volatility <= 3:

            return 20


        elif market_volatility <= 5:

            return 10


        return 0


    # -------------------------------------

    def drawdown_score(

        self,

        drawdown

    ):

        """
        Market drawdown
        """


        if drawdown <= 5:

            return 20


        elif drawdown <= 10:

            return 15


        elif drawdown <= 20:

            return 10


        return 0


    # -------------------------------------

    def calculate(

        self,

        atr_percent,

        market_volatility,

        drawdown

    ):

        """
        Final volatility score
        """


        score = 0


        score += self.atr_score(

            atr_percent

        )


        score += self.index_volatility_score(

            market_volatility

        )


        score += self.drawdown_score(

            drawdown

        )


        if score > 100:

            score = 100


        return score