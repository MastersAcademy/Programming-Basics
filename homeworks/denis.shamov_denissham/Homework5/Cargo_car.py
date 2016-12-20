from Vehicle import Vehicle

class Cargo_car:
    def __init__(self, wheels_quantity, move_from, move_to, combustion_engine, can_move_cargo):
        Vehicle.__init__(self, wheels_quantity, move_from, move_to, combustion_engine, 'Cargo_car')
        self.can_move_cargo = can_move_cargo

    def move_cargo(self):
        return "Scania Streamline"

    def move_passangers(self):
        return "I can`t do this"

    def change_move_to(self):
        return "Ok! lets go to another city!"