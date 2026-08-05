"""
Iran AI Trader Professional

Scanner Regime Filter
Sprint39

Market condition filter for scanner
"""


class ScannerRegimeFilter:


    def __init__(self):

        pass



    # -------------------------------------

    def check(

        self,

        regime,

        score

    ):

        """
        Check if scanner can generate buy signals
        """


        regime = regime.upper()



        result = {


            "allowed": False,

            "mode": "BLOCK",

            "reason": ""

        }



        # Strong Bull / Bull

        if regime in [

            "STRONG BULL",

            "BULL"

        ]:


            if score >= 70:


                result["allowed"] = True

                result["mode"] = "NORMAL"

                result["reason"] = "Bull market condition"



            else:


                result["mode"] = "WATCH"

                result["reason"] = "Score below threshold"



        # Early Bull

        elif regime == "EARLY BULL":


            if score >= 75:


                result["allowed"] = True

                result["mode"] = "CAUTIOUS"

                result["reason"] = "Early bull confirmation"



            else:


                result["mode"] = "WATCH"

                result["reason"] = "Waiting confirmation"



        # Sideways

        elif regime == "SIDEWAYS":


            if score >= 85:


                result["allowed"] = True

                result["mode"] = "SELECTIVE"

                result["reason"] = "Strong stock in sideways market"



            else:


                result["mode"] = "WATCH"

                result["reason"] = "Sideways market"



        # Bear

        elif regime == "BEAR":


            result["allowed"] = False

            result["mode"] = "RISK"

            result["reason"] = "Bear market protection"



        # Strong Bear

        else:


            result["allowed"] = False

            result["mode"] = "BLOCK"

            result["reason"] = "Extreme risk"



        return result