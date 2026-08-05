from scanner_v2.validator import Validator



class FakeHistory:


    def close_prices(self):

        return [

            100 + i

            for i in range(25)

        ]





validator = Validator()



history_ok = validator.validate_history(

    FakeHistory(),

    "TEST1"

)



score_ok = validator.validate_score(

    75

)



score_bad = validator.validate_score(

    150

)



print()

print("=" * 60)

print("VALIDATOR V2 TEST")

print("=" * 60)

print()


print(

    "History Valid:",

    history_ok

)


print(

    "Score 75:",

    score_ok

)


print(

    "Score 150:",

    score_bad

)


print(

    "Rejected:",

    validator.rejected_count()

)


print()

print("TEST FINISHED")