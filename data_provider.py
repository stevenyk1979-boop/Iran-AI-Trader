"""
Iran AI Trader V2.0 Alpha
Data Provider Layer

این کلاس تنها مسئول دریافت داده از منبع داده است.
در حال حاضر از CSV استفاده می‌کنیم.
بعداً فقط همین فایل به TSETMC یا API واقعی متصل خواهد شد.
"""

from csv_loader import CSVLoader


class DataProvider:

    def __init__(self):

        self.loader = CSVLoader()

    def load_history(self, filename="historical_data.csv"):

        """
        بارگذاری اطلاعات تاریخی
        """

        return self.loader.load(filename)

    def get_prices(self, filename="historical_data.csv"):

        """
        فقط قیمت‌های پایانی
        """

        history = self.load_history(filename)

        return history.close_prices()

    def get_last_record(self, filename="historical_data.csv"):

        """
        آخرین رکورد
        """

        history = self.load_history(filename)

        return history.last()

    def get_symbol(self, filename="historical_data.csv"):

        """
        نام نماد
        """

        last = self.get_last_record(filename)

        if last:

            return last.symbol

        return None