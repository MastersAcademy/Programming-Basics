from Apple import Apple
from random import randint

class RedApple(Apple):
    def __init__(self, name, weight, last_day, price, can_discount):
        Apple.__init__(self, name, weight, last_day, 100)
        self.can_discount = can_discount

    def __set_discount(self):
        discount_value = randint(2, 20)

        price = self.price

        price = int(price * (100 - discount_value) / 100)

        result = {
            'discount': discount_value,
            'total_price': price
        }

        return result


    def __getPrice(self):
        if self.can_discount == 'true':
            data = self.__set_discount()
            return 'You are lucky, today you get discount \'%s\' procents and you needs pay \'%s\' dollars instead of paying \'%s\' dollars. Have a nice day!' % (data['discount'], data['total_price'], self.price)
        else:
            return 'You need pay \'%s\' dollars. Have a nice day!' % self.price
