class blender(object):
    def __init__(self, brand, wattage, color, material, size, weight):
        self.brand = brand
        self.wattage = wattage
        self.color = color
        self.material = material
        self.size = size
        self. weight = weight

    def description_of_blender(self):
        print("-------------------------------------")
        print("The brand is",self.brand)
        print("The wattage is",self.wattage, "W")
        print("The color is", self.color)
        print("The material is", self.material)
        print("The size is", self.size, "sm")
        print("The weight is", self.weight, "kg")

    # инкапсуляция
    def what_are_intersting_inside(self):
        print("-------------------------------------")
        print("Caution. Do not reveal the panel. It may be dangerously for health.")