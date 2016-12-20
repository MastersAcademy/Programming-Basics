class TennisRacket:

    racket_list = []

    def __init__(self, grip_size, square_head, weight, brand):
        self.grip_size = grip_size
        self.square_head = square_head
        self.weight = weight
        self.brand = brand

    def add_racket(self):
        self.racket_list = [self.grip_size, self.square_head, self.weight, self.brand]
        return self.racket_list




