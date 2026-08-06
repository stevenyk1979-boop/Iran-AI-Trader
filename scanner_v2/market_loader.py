"""
Iran AI Trader Professional

Scanner V2

Sprint44-10

Market Loader Adapter Connected
"""


from scanner_v2.market_adapter import MarketAdapter



class MarketLoader:


    def __init__(
        self,
        adapter=None
    ):


        self.adapter = adapter or MarketAdapter()



        self.symbols = [

            {
                "symbol": "TEST1"
            },

            {
                "symbol": "TEST2"
            }

        ]




    def load_symbols(
        self,
        data=None
    ):


        try:


            if data is None:


                adapter_symbols = self.adapter.get_symbols()



                if adapter_symbols:

                    return adapter_symbols



                data = self.symbols



            result = []



            for item in data:


                if item is None:

                    continue



                if "symbol" not in item:

                    continue



                result.append(

                    item["symbol"]

                )



            self.symbols = result



            return result



        except Exception:


            return []





    def count(self):


        return len(

            self.symbols

        )