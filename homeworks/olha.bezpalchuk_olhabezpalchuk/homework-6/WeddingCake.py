from Cake import Cake


class WeddingCake(Cake):
    def __init__(self, name, ingredients, price, jewelry):
        super(WeddingCake, self).__init__(name, ingredients, price)
        self.jewelry = jewelry

    def add_jewelry(self, jewelry):
        self.jewelry.add(jewelry)
