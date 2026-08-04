"""
Iran AI Trader Professional
Correlation Engine Test
Sprint33-C
"""


from correlation_engine import CorrelationEngine
from correlation_report import CorrelationReport



def main():


    print()

    print("=" * 70)

    print(

        "CORRELATION ENGINE TEST"

    )

    print("=" * 70)



    price_history = {


        "چکارن": [

            100,

            102,

            105,

            108,

            110

        ],



        "ولملت": [

            200,

            204,

            210,

            216,

            220

        ],



        "دزاگرس": [

            300,

            299,

            301,

            298,

            305

        ]

    }



    engine = CorrelationEngine()



    result = engine.analyze(

        price_history

    )



    report = CorrelationReport()



    report.show(

        result

    )



if __name__ == "__main__":

    main()