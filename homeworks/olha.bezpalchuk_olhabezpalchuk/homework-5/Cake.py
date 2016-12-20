class Cake(object):
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.cooking_method = "Default method: just mix all ingredients." + str(self.ingredients)

    def __str__(self):
        return "Cake %s, %.2f\n" % (self.name, self.price) + str(self.ingredients)

    def change_cooking_method(self, cooking_method):
        self.cooking_method = cooking_method

    def cooking_method(self):
        return self.cooking_method

    def add_ingredient(self, ingredient):
        self.ingredients.add(ingredient)
