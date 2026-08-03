"""
Iran AI Trader Professional
Smart Money Adapter
Sprint31-B
"""


from smart_money_engine import SmartMoneyEngine



class SmartMoneyAdapter:


    def __init__(self):

        self.engine = SmartMoneyEngine()



    # -------------------------------------

    def calculate_score(

        self,

        item

    ):

        """
        Convert ranking item
        into smart money analysis
        """


        data = {


            "symbol": item.get(

                "symbol"

            ),


            "volume_ratio": item.get(

                "volume_ratio",

                0

            ),


            "buyer_power": item.get(

                "buyer_power",

                0

            )

        }



        result = self.engine.analyze(

            data

        )


        return result



    # -------------------------------------

    def apply(

        self,

        item

    ):

        """
        Add Smart Money score
        to ranking item
        """


        result = self.calculate_score(

            item

        )


        item["smart_money_score"] = result["score"]


        item["smart_money_status"] = result["status"]


        item["smart_money_signals"] = result["signals"]



        return item