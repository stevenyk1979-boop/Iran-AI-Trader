"""
Iran AI Trader Professional
Trade Candidate Engine
Sprint28-D
"""


class TradeCandidateEngine:


    def __init__(self):

        pass



    # -------------------------------------

    def classify(self, validation):

        """
        Classify entry validation result
        """

        status = validation.get(

            "status",

            "WAIT"

        )


        if status == "READY TO BUY":

            return "READY"


        elif status == "WATCH":

            return "WATCH"


        else:

            return "REJECT"



    # -------------------------------------

    def create_candidate(

        self,

        item,

        validation

    ):

        """

        Create trade candidate object

        """


        category = self.classify(

            validation

        )


        return {


            "symbol": item.get(

                "symbol"

            ),


            "score": item.get(

                "score",

                0

            ),


            "signal": item.get(

                "signal",

                "HOLD"

            ),


            "confidence": item.get(

                "confidence",

                0

            ),


            "risk": item.get(

                "risk",

                0

            ),


            "category": category,


            "validation": validation

        }



    # -------------------------------------

    def generate(

        self,

        watchlist,

        validator

    ):

        """

        Generate candidates from watch list

        """


        candidates = []


        for item in watchlist:


            validation = validator.validate(

                item

            )


            candidate = self.create_candidate(

                item,

                validation

            )


            candidates.append(

                candidate

            )


        candidates.sort(

            key=lambda x: x["score"],

            reverse=True

        )


        return candidates