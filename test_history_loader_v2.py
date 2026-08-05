from scanner_v2.history_loader import HistoryLoader



class FakeHistory:


    def __init__(self):

        self.prices = [

            100 + i

            for i in range(25)

        ]



    def close_prices(self):

        return self.prices





class FakeMarketService:


    def history(self, symbol):

        return FakeHistory()





loader = HistoryLoader(

    FakeMarketService()

)



history = loader.load_history(

    "TEST1"

)



print()

print("=" * 60)

print("HISTORY LOADER V2 TEST")

print("=" * 60)


print()


print(

    "Valid:",

    loader.validate_history(history)

)


print(

    "Failed:",

    loader.failed_count()

)


print()

print("TEST FINISHED")