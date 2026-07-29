"""
Iran AI Trader Professional
TSETMC History Provider
"""


from datetime import datetime, timedelta



class TSETMCHistory:


    def __init__(self, connector=None):

        self.connector = connector



    def get_history(self, symbol, days=30):

        """
        Get historical candles for symbol

        Output format:

        [
            [
                date,
                open,
                high,
                low,
                close,
                volume
            ]
        ]

        """


        # TODO:
        # Replace with real TSETMC API


        records = []


        price = 100


        today = datetime.now()



        for i in range(days):


            date = (

                today - timedelta(days=days-i)

            ).strftime("%Y-%m-%d")



            records.append([

                date,

                price,

                price + 2,

                price - 2,

                price + 1,

                1000000

            ])


            price += 1



        return records



    def is_available(self):

        """
        Check provider status
        """

        return True