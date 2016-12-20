class Cognac:
    def __init__(self, colour, strength, country_of_product, grape_sort):
        self.colour = colour
        self.strenght = strength
        self.country_of_product = country_of_product
        self.grape_sort = grape_sort

    def description(self):
        return "Cognac description:\nThe colour: %s,\nVol: %i,\nCountry: %s,\nGrape sort: %s " \
               % (self.colour, self.strenght, self.country_of_product, self.grape_sort)