"""
Iran AI Trader Professional
Capital Report Test
Sprint32-F
"""

from capital_report import CapitalReport


def main():

    report = CapitalReport()


    decision = {

        "symbol": "چکارن",

        "signal": "BUY",

        "score": 96.43,

        "capital": {

            "allowed": True,

            "allocation_percent": 5,

            "capital": 5000000,

            "shares": 196,

            "capital_used": 4980000

        }

    }


    print()

    report.show(

        decision

    )


if __name__ == "__main__":

    main()