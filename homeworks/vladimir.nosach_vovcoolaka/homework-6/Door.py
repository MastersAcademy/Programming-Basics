class Door(object):
    def __init__(self, model, width, length, color, factory_number):
        self.model = model
        self.width = width
        self.length = length
        self.color = color
        self.factory_number = factory_number

    def description_of_door(self):
        print(".............................................")
        print("| The model of door", self.factory_number, "is:", self.model)
        print("| The dimensions of door", self.factory_number, "is:", self.width, "x", self.length, "cm")
        print("| The color of door", self.factory_number, "is:", self.color)




