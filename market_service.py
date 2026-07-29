"""
Iran AI Trader Professional
Market Service
"""


from market_repository import MarketRepository
from download_manager import DownloadManager



class MarketService:


    def __init__(self):

        self.repository = MarketRepository()

        self.downloader = DownloadManager()

        self.downloader.connect()



    def get_history(self, filename="historical_data.csv"):

        return self.repository.history(filename)



    def get_prices(self, filename="historical_data.csv"):

        """
        Return prices.
        If data file does not exist,
        download history first.
        """

        try:

            return self.repository.prices(filename)


        except FileNotFoundError:


            symbol = self.extract_symbol(filename)


            if symbol:


                self.downloader.download_history(symbol)


                return self.repository.prices(filename)



            return []



    def extract_symbol(self, filename):

        """
        Extract symbol name from path

        Example:
        market_data/وبملت.csv
        """

        if "/" in filename:

            name = filename.split("/")[-1]

        elif "\\" in filename:

            name = filename.split("\\")[-1]

        else:

            name = filename



        if name.endswith(".csv"):

            name = name[:-4]


        if name == "historical_data":

            return None


        return name



    def get_last_symbol(self, filename="historical_data.csv"):

        return self.repository.symbol(filename)