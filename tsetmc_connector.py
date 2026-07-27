"""
Iran AI Trader V2.0 Alpha
TSETMC Connector
"""


class TSETMCConnector:

    def __init__(self):

        self.connected = False

    def connect(self):

        """
        اتصال آزمایشی
        """

        self.connected = True

        return True

    def status(self):

        return self.connected

    def get_symbols(self):

        """
        فعلاً داده آزمایشی
        """

        return [

            "وبملت",

            "فملی",

            "فولاد",

            "شستا",

            "خودرو"

        ]