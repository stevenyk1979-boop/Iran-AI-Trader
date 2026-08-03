"""
Iran AI Trader Professional
Entry Validator Test
Sprint28-C
"""


from entry_validator import EntryValidator



def main():


    validator = EntryValidator()


    test_result = {


        "symbol": "چکارن",

        "score": 94.9,

        "confidence": 100,

        "risk": 11,

        "signal": "STRONG BUY"

    }



    result = validator.validate(

        test_result

    )



    print()

    print("=" * 60)

    print("ENTRY VALIDATOR TEST")

    print("=" * 60)



    print(

        "Symbol:",

        test_result["symbol"]

    )


    print(

        "Score:",

        test_result["score"]

    )


    print(

        "Signal:",

        test_result["signal"]

    )


    print()

    print(

        "Validation Status:",

        result["status"]

    )


    print(

        "Checks:",

        result["checks"]

    )


    print(

        "Passed:",

        result["passed"],

        "/",

        result["total"]

    )



    print("=" * 60)



if __name__ == "__main__":

    main()