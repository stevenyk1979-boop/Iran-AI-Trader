from scanner_v2.market_loader import MarketLoader



loader = MarketLoader()



sample_data = [

    {
        "symbol": "TEST1"
    },

    {
        "symbol": "TEST2"
    },

    {
        "name": "BAD"
    }

]



symbols = loader.load_symbols(

    sample_data

)



print()

print("=" * 60)

print("MARKET LOADER V2 TEST")

print("=" * 60)



print()

print(

    "Loaded:",

    len(symbols)

)



for item in symbols:

    print(

        item["symbol"]

    )



print()

print("TEST FINISHED")