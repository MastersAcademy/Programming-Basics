class Salad:

    __privet_corn = 'this special ingredient only for first salad your make'

    def __init__(self, ingredient1, ingredient2, ingredient3, tainiy_ingredient):
        self.ingredient1 = ingredient1
        self.ingredient2 = ingredient2
        self.ingredient3 = ingredient3
        self.tainiy_ingredient = tainiy_ingredient
        self.__privet_corn = 'secret ingredient'

    def __str__(self):
        return "|- In your salad you have: %s, %s, %s, %s, %s " %(self.ingredient1, self.ingredient2, self.ingredient3, self.tainiy_ingredient, self.__privet_corn)

    def thought(self):
        return "|-=- You have salad, congratulation"
