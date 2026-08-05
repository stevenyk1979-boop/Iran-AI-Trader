"""
Iran AI Trader Professional

Regime Weight Engine
Sprint38.5

Adjust scoring weights according to market regime
"""


class RegimeWeightEngine:


    def __init__(self):

        pass



    # -------------------------------------

    def get_weights(self, regime):

        """
        Dynamic scoring weights
        """


        regime = regime.upper()



        # Bull Market
        if regime == "BULL" or regime == "STRONG BULL":


            return {


                "technical": 1.20,

                "momentum": 1.15,

                "liquidity": 1.10,

                "risk": 0.90

            }



        # Early Bull

        elif regime == "EARLY BULL":


            return {


                "technical": 1.10,

                "momentum": 1.10,

                "liquidity": 1.05,

                "risk": 1.00

            }



        # Sideways

        elif regime == "SIDEWAYS":


            return {


                "technical": 1.00,

                "momentum": 0.90,

                "liquidity": 1.00,

                "risk": 1.20

            }



        # Bear

        elif regime == "BEAR":


            return {


                "technical": 0.80,

                "momentum": 0.70,

                "liquidity": 0.90,

                "risk": 1.40

            }



        # Strong Bear

        else:


            return {


                "technical": 0.60,

                "momentum": 0.50,

                "liquidity": 0.70,

                "risk": 1.60

            }