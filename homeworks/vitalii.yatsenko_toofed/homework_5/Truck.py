from Car import Car

class Truck(Car):
    def __init__(self, count_wheels, engine, body, max_weight):
        Car.__init__(self, count_wheels, engine, body)
        self.max_weight = max_weight
        self.loaded_weight = 0

    def load_weight(self, weight):
        self.loaded_weight += weight
        if self.loaded_weight < self.max_weight:
            return "load complete"
        else:
            return "max_weight exceeded"

    def drive(self):
        if self.engine_status == True:
            return 'Wroom Wroom'
        else:
            return 'start engine before'




