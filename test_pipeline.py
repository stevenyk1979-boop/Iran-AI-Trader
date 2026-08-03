"""
Iran AI Trader Professional
Pipeline Test
Sprint29-B
"""


from pipeline import TradingPipeline



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



def main():


    watchlist = [


        {

            "symbol": "چکارن",

            "score": 94.9,

            "confidence": 100,

            "risk": 11,

            "signal": "STRONG BUY"

        },


        {

            "symbol": "پتایر",

            "score": 80,

            "confidence": 70,

            "risk": 25,

            "signal": "BUY"

        },


        {

            "symbol": "فایرا",

            "score": 28,

            "confidence": 33,

            "risk": 30,

            "signal": "SELL"

        }

    ]



    pipeline = TradingPipeline(

        FakeValidator()

    )


    result = pipeline.run(

        watchlist,

        total_symbols=914

    )



    print()

    print("=" * 60)

    print("PIPELINE TEST")

    print("=" * 60)



    for item in result["decisions"]:


        print(

            item["symbol"],

            "=>",

            item["decision"]

        )



    print("=" * 60)



if __name__ == "__main__":

    main()