from Salad import *

class Salad2(Salad):


    def __init__(self, ingredient1, ingredient2, tainiy_ingredient, ingredient4, mayona):
        Salad.__init__(self, ingredient1, ingredient2, 'ingredient3', tainiy_ingredient)
        self.ingredient4 = ingredient4
        self.mayona = mayona

    def __str__(self):
        return "|- In your second salad you have: %s, %s, %s, %s, %s " %(self.ingredient1, self.ingredient2, self.tainiy_ingredient, self.ingredient4, self.mayona)

    def thought_about_second_salat(self):
        return "|-=- You have new salad, congratulation"
