"""
Iran AI Trader Professional
Capital Allocation Report Test
Sprint32-G
"""


from capital_allocation_report import CapitalAllocationReport



def main():


    report = CapitalAllocationReport()


    decisions = [


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



    report.show(

        decisions

    )



if __name__ == "__main__":

    main()