from TennisRaquet import TennisRacket


class TennisRacketPrice(TennisRacket):

    def __init__(self, grip_size, square_head, weight, brand):
        TennisRacket.__init__(self, grip_size, square_head, weight, brand)

    def add_price(self, price):
        self.price = price
        self.racket_list = self.add_racket()
        self.racket_list.append(self.price)
        return self.racket_list
