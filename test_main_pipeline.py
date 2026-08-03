"""
Iran AI Trader Professional
Main Pipeline Test
Sprint29-C
"""

from main_pipeline import MainPipeline


class FakeScanner:

    def watchlist(self):

        return [

            {

                "symbol": "چکارن",

                "score": 94.9,

                "confidence": 100,

                "risk": 11,

                "signal": "BUY"

            },

            {

                "symbol": "پتایر",

                "score": 80,

                "confidence": 70,

                "risk": 20,

                "signal": "BUY"

            },

            {

                "symbol": "فایرا",

                "score": 28,

                "confidence": 30,

                "risk": 35,

                "signal": "SELL"

            }

        ]


class FakeValidator:

    def validate(

        self,

        item

    ):

        if item["score"] >= 85:

            return {

                "status": "READY TO BUY"

            }

        elif item["score"] >= 60:

            return {

                "status": "WATCH"

            }

        else:

            return {

                "status": "REJECT"

            }


pipeline = MainPipeline(

    FakeValidator(),

    FakeScanner()

)

result = pipeline.run()

print()

print("=" * 60)

print("MAIN PIPELINE TEST")

print("=" * 60)

for d in result["decisions"]:

    print(

        d["symbol"],

        "=>",

        d["decision"]

    )

print("=" * 60)