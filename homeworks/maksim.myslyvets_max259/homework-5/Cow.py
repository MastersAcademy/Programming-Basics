from Mammals import Mammals



class Cow(Mammals):
    def __init__(self, viviparous, warm_blooded, wool, mammals, giving_meat, geaving_milk,):
        self.increased_endurance = giving_meat
        self.ruggledness = geaving_milk


    def __str__(self):
        return "viviparous: %s, warm_blooded: %s, wool: %s, mammals: %s, giving_meat: %s, geaving_milk: %s" % (self.viviparous, self.warm_blooded, self.wool, self.mammals, self.giving_meat, self.geaving_milk)