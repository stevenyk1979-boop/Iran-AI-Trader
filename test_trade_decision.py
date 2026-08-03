"""
Iran AI Trader Professional
Trade Decision Test
Sprint28-E
"""


from trade_decision import TradeDecisionEngine



def main():


    engine = TradeDecisionEngine()



    candidates = [


        {

            "symbol": "چکارن",

            "category": "READY",

            "score": 94.9,

            "confidence": 100,

            "risk": 11

        },


        {

            "symbol": "پتایر",

            "category": "WATCH",

            "score": 80,

            "confidence": 70,

            "risk": 25

        },


        {

            "symbol": "فایرا",

            "category": "REJECT",

            "score": 28,

            "confidence": 33,

            "risk": 30

        }

    ]



    print()

    print("=" * 60)

    print("TRADE DECISION TEST")

    print("=" * 60)



    for item in candidates:


        result = engine.decide(item)


        print(

            result["symbol"],

            "=>",

            result["decision"]

        )


        print(

            "Reasons:",

            result["reasons"]

        )


        print("-" * 60)



if __name__ == "__main__":

    main()