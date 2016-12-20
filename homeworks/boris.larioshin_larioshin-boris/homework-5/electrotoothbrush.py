from toothbrush import ToothBrush
from battery import Battery


class ElectricToothBrush(ToothBrush):
    def __init__(self, title, bristles_type, platform_material, handle_len, purchase_year, purchase_month, purchase_day, battery):
        ToothBrush.__init__(self, title, bristles_type, platform_material, handle_len, purchase_year, purchase_month, purchase_day, expiration_date=120)
        self.battery = Battery(battery)

    # Перевизначена дія чистити
    def clean(self):
        return print('Для чищення натисніть кнопку на щітці ' + self.title + '. Нехай вона сама працює! ')

    # Виведення інформації та інфо про батарейку
    def about_electric_brush(self):
        self.about_brush()
        self.battery.battery_info()

