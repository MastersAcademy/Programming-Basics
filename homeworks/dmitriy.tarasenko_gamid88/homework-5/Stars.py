from Cognac import Cognac

class CognacOld(Cognac):
    def __init__(self, colour, strength, country_of_product, grape_sort, number_of_stars):
        super().__init__(colour, strength, country_of_product, grape_sort)
        self.number_of_stars = number_of_stars

    def description_with_stars(self):
        return "Cognac description:\nThe colour: %s,\nVol: %i,\nCountry: %s,\nGrape sort: %s, \nNumber of stars: %i" \
               % (self.colour, self.strenght, self.country_of_product, self.grape_sort, self.number_of_stars)