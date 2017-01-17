from Vehicle import Vehicle

class Car:
    def __init__(self, wheels_quantity, move_from, move_to, combustion_engine, can_move_passangers):
        Vehicle.__init__(self, wheels_quantity, move_from, move_to, combustion_engine, 'car')
        self.can_move_passangers = can_move_passangers


    def move_passangers(self):
        return "Maserati Quattroporte"

    def move_cargo(self):
        return "I can`t do this"

    def change_move_to(self):
        return "Ok! lets go to another city!"


