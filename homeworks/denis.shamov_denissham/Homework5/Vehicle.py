class Vehicle:
    def __init__(self, wheels_quantity, move_from, move_to, combustion_engine, type):
        self.wheels_quantity = wheels_quantity
        self.move_from = move_from
        self.move_to = move_to
        self.combustion_engine = combustion_engine
        self.type = type

    def __str__(self):
        return "Wheels quantity: %s\n Move from: %s\n Move to: %s\n Combustion engine: %s\n Type: %s\n" % (self.wheels_quantity, self.move_from, self.move_to, self.combustion_engine, self.type)


    def vehicle_data(self):
        return "%s %s %s %s" % (self.wheels_quantity, self.move_from, self.move_to, self.combustion_engine)