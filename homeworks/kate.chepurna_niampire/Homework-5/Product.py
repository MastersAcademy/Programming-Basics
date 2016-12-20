class Product(object):
    def __init__(self, produt_name, weight, last_day, price):
        self.produt_name = produt_name
        self.weight = weight
        self.last_day = last_day
        self.price = price

    def successful_message(self):
        return 'Congratulations, product \'%s\' successfully added! Have a nice day!' % self.produt_name
