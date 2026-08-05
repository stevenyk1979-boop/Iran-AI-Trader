"""
Iran AI Trader Professional

Scanner Regime Bridge
Sprint39.5

Connect Market Regime with Scanner Decision
"""


from .scanner_regime_filter import ScannerRegimeFilter



class ScannerRegimeBridge:


    def __init__(self):

        self.filter = ScannerRegimeFilter()



    # -------------------------------------

    def evaluate(

        self,

        regime,

        market_score,

        stock_score

    ):

        """
        Evaluate scanner permission
        """



        filter_result = self.filter.check(

            regime,

            market_score

        )



        decision = {


            "allowed": filter_result["allowed"],

            "mode": filter_result["mode"],

            "reason": filter_result["reason"],

            "regime": regime,

            "market_score": market_score,

            "stock_score": stock_score,

            "action": "BLOCK"

        }



        # ---------------------------------
        # Trading Action
        # ---------------------------------


        if filter_result["allowed"]:


            if stock_score >= 85:


                decision["action"] = "BUY_READY"



            elif stock_score >= 70:


                decision["action"] = "WATCH"



            else:


                decision["action"] = "IGNORE"



        else:


            decision["action"] = "RISK_BLOCK"



        return decision