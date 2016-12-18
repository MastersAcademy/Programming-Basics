from Mammals import Mammals



class Horse(Mammals):
    def __init__(self, viviparous, warm_blooded, wool, mammals, race, carry_things,):
        self.increased_endurance = race
        self.ruggledness = carry_things


    def __str__(self):
        return "viviparous: %s, warm_blooded: %s, wool: %s, mammals: %s, race: %s, carry_things: %s" % (self.viviparous, self.warm_blooded, self.wool, self.mammals, self.race, self.carry_things)