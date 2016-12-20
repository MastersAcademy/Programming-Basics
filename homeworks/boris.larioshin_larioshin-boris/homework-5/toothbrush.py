from brush import Brush
from datetime import date


class ToothBrush(Brush):
    def __init__(self, title, bristles_type, platform_material, handle_len, purchase_year, purchase_month, purchase_day, expiration_date=90):
        Brush.__init__(self, title, bristles_type, platform_material)
        self.handle_len = handle_len
        self.purchase_year = purchase_year
        self.purchase_month = purchase_month
        self.purchase_day = purchase_day
        self.expiration_date = expiration_date

    def __str__(self):
        return "Торгівельна марка: %s, тип щєтини: %s, матеріал платформи: %s, довжина ручки: %s" % (self.title, self.bristles_types, self.platform_material, self.handle_len)

    # Дія чистити
    def clean(self):
        return print('Для чищення робіть рухи зубною щіткою' + self.title + 'вздовж та впоперек ротової порожнини' + '\n')

    # Дата придбання
    def purchase_date(self):
        return date(self.purchase_year, self.purchase_month, self.purchase_day)

    # Перевірка чи не треба замінити зубну щітку
    def applicability(self):
        today = date.today()
        delta = today - self.purchase_date()

        if delta.days > self.expiration_date:
            return print('Треба замінити зубну щітку. Вона вже своє відпрацювала.' + '\n')
        else:
            return print('Зубна щітка не так давно придбана. Ще можна користуватися.' + '\n')

    # Виведення інформації
    def about_brush(self):
        print('***********************About brush***********************************')
        print('Торгівельна марка: ' + self.title + '\n')
        print('Тип щєтини: ' + self.bristles_types + '\n')
        print('Матеріал для платформи: ' + self.platform_material + '\n')
        print("Довжина ручки: " + str(self.handle_len) + '\n')
        self.applicability()
