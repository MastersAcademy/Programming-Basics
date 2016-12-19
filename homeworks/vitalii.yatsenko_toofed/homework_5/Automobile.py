from Car import Car

class Automobile(Car):
    def __init__(self, count_wheels, engine, body, max_passengers):
        Car.__init__(self, count_wheels, engine, body)
        self.max_passengers = max_passengers
        self.loaded_passengers = 0

    def load_passenger(self, passeng_count):
        self.loaded_passengers += passeng_count
        if self.loaded_passengers < self.max_passengers:
            return "load passengers completed"
        else:
            return "max_passengers exceeded"


