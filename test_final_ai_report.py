"""
Iran AI Trader Professional
Final AI Report Test
Sprint32-H
"""


from final_ai_report import FinalAIReport



def main():


    report = FinalAIReport()


    data = {


        "regime": {

            "regime": "BEAR",

            "score": 46.05,

            "confidence": 70

        },


        "candidates": [

            {

                "symbol": "چکارن"

            },

            {

                "symbol": "ولملت"

            }

        ],


        "decisions": [


            {

                "symbol": "چکارن",

                "score": 96.43,

                "signal": "BUY",

                "capital": {

                    "allowed": True,

                    "capital": 5000000,

                    "shares": 196

                }

            },


            {

                "symbol": "ولملت",

                "score": 91,

                "signal": "BUY",

                "capital": {

                    "allowed": True,

                    "capital": 3000000,

                    "shares": 150

                }

            }

        ]

    }



    report.show(

        data

    )



if __name__ == "__main__":

    main()