from scanner_v2.ranking_engine import RankingEngine



class FakeHistory:


    def close_prices(self):

        return [

            100,

            101,

            102,

            103,

            104,

            105,

            106,

            107,

            108,

            109,

            110,

            111,

            112,

            113,

            114,

            115,

            116,

            117,

            118,

            119,

            120

        ]




engine = RankingEngine()



result = engine.analyze(

    FakeHistory(),

    "TEST1"

)



print()

print("=" * 60)

print("RANKING ENGINE V2 TEST")

print("=" * 60)

print()


print(

    result

)


print()

print("TEST FINISHED")