from Product import Product

class Apple(Product):
    def __init__(self, name, weight, last_day, price):
        Product.__init__(self, name, weight, last_day, price)


