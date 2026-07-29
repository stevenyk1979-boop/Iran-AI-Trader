"""
Iran AI Trader Professional
Download Manager
"""

from history_downloader import HistoryDownloader



class DownloadManager:


    def __init__(self):

        self.connected = False

        self.downloader = HistoryDownloader()



    def connect(self):

        """
        Initialize downloader
        """

        self.connected = True

        return True



    def status(self):

        return self.connected



    def download_history(self, symbol):

        """
        Download historical data for symbol
        """

        if not self.connected:

            self.connect()


        return self.downloader.download(symbol)



    def get_cached_history(self, symbol):

        """
        Return cached history file
        """

        if self.downloader.exists(symbol):

            return self.downloader.file_path(symbol)


        return None



    def cache_exists(self, symbol):

        """
        Check cache status
        """

        return self.downloader.exists(symbol)