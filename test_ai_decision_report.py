"""
Iran AI Trader Professional
AI Decision Report Test
Sprint28-F
"""


from ai_decision_report import AIDecisionReport



def main():


    decisions = [


        {

            "symbol": "چکارن",

            "decision": "BUY",

            "score": 94.9,

            "confidence": 100,

            "risk": 11,

            "reasons": [

                "Entry validation passed",

                "Strong AI score",

                "High confidence"

            ]

        },


        {

            "symbol": "پتایر",

            "decision": "WAIT",

            "score": 80,

            "confidence": 70,

            "risk": 25,

            "reasons": [

                "Waiting for confirmation"

            ]

        },


        {

            "symbol": "فایرا",

            "decision": "IGNORE",

            "score": 28,

            "confidence": 33,

            "risk": 30,

            "reasons": [

                "Candidate rejected"

            ]

        }

    ]



    engine = AIDecisionReport()


    report = engine.generate(

        decisions

    )


    engine.print_report(

        report

    )



if __name__ == "__main__":

    main()