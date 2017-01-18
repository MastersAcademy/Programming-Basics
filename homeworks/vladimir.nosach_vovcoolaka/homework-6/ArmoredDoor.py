from Door import Door

class ArmoredDoor(Door):
    def __init__(self, model, width, length, color, factory_number, lock_type):
        Door.__init__(self, model, width, length, color, factory_number)
        self.lock_type = lock_type
    def description_of_door(self):
        super().description_of_door()
        print("| The type of lock in door", self.factory_number, "is:", self.lock_type)

