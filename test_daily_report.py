"""
Iran AI Trader Professional
Daily Report Test
Sprint29-A
"""


from daily_report import DailyReport



def main():


    decisions = [


        {

            "symbol": "چکارن",

            "decision": "BUY",

            "score": 94.9

        },


        {

            "symbol": "پتایر",

            "decision": "WAIT",

            "score": 80

        },


        {

            "symbol": "فایرا",

            "decision": "IGNORE",

            "score": 28

        }

    ]



    report_engine = DailyReport()



    report = report_engine.generate(

        decisions,

        total_symbols=914,

        watchlist_size=100

    )



    report_engine.print_report(

        report

    )



if __name__ == "__main__":

    main()