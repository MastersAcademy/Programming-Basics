



class Product(object):
    def __init__(self, produt_name, weight, last_day, price):
        self.produt_name = produt_name
        self.weight = weight
        self.last_day = last_day
        self.price = price

    def successful_message(self):
        return 'Congratulations, product \'%s\' successfully added! Have a nice day!' % self.produt_name


def getPrice(self):
    if self.can_discount == 'true':
        data = self.__set_discount()
        return 'You are lucky, today you get discount \'%s\' procents and you needs pay \'%s\' dollars instead of paying \'%s\' dollars. Have a nice day!' % (
        data['discount'], data['total_price'], self.price)
    else:
        return 'You need pay \'%s\' dollars. Have a nice day!' % self.price
