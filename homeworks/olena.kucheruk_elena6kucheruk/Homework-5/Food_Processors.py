from blender import blender

class Food_Processors(blender):
    def __init__(self, brand, wattage, color, material, size, weight, have_additional_function):
        blender.__init__(self, brand, wattage, color, material, size, weight)
        self.have_additional_function = have_additional_function

    def description_of_food(self):
        print("-------------------------------------")
        print("The brand is", self.brand)
        print("The wattage is", self.wattage, "W")
        print("The color is", self.color)
        print("The material is", self.material)
        print("The size is", self.size, "sm")
        print("The weight is", self.weight, "kg")
        print ("Have additional function")

    def in_the_shop(self):
        print ("-------------------------------------")
        print ("It will be good thing on the kitchen")
# инкапсуляция
    def what_are_intersting_inside(self):
        print("-------------------------------------")
        print ("Caution. Do not reveal the panel. It may be dangerously for health.")

Food_Processors1 = Food_Processors ('Kenwood', '1400', 'white', 'steal', '40', '3', 'have')
Food_Processors1.description_of_food()
Food_Processors1.in_the_shop()
Food_Processors1.what_are_intersting_inside()