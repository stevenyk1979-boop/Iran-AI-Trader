"""
Iran AI Trader Professional
Trade Candidate Test
Sprint28-D
"""


from trade_candidate import TradeCandidateEngine
from entry_validator import EntryValidator



def main():


    validator = EntryValidator()

    engine = TradeCandidateEngine()



    watchlist = [


        {

            "symbol": "چکارن",

            "score": 94.9,

            "confidence": 100,

            "risk": 11,

            "signal": "STRONG BUY"

        },


        {

            "symbol": "فایرا",

            "score": 28.7,

            "confidence": 33,

            "risk": 30,

            "signal": "SELL"

        }


    ]



    result = engine.generate(

        watchlist,

        validator

    )


    print()

    print("=" * 60)

    print("TRADE CANDIDATE TEST")

    print("=" * 60)



    for item in result:

        print(

            item["symbol"],

            "|",

            item["category"],

            "| Score:",

            item["score"]

        )


    print("=" * 60)



if __name__ == "__main__":

    main()