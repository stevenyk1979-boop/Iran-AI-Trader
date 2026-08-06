from scanner_v2.scanner import Scanner


class FakeHistory:


    def close_prices(self):

        return [

            100 + i

            for i in range(30)

        ]



class FakeMarketService:


    def history(self, symbol):

        return FakeHistory()



class FakeMarketLoader:


    def load_symbols(self):

        return [

            "TEST1",

            "TEST2"

        ]



scanner = Scanner()


scanner.market_loader = FakeMarketLoader()

scanner.history_loader.market_service = FakeMarketService()



results = scanner.scan()



print()

print("=" * 60)

print("SCANNER V2 TEST")

print("=" * 60)

print()


print(

    "Results:"

)


for item in results:

    print(item)



print()

print(

    "TEST FINISHED"

)