from Mammals import Mammals



class Donkey(Mammals):
    def __init__(self, viviparous, warm_blooded, wool, mammals, increased_endurance, ruggledness, long_ears):
        self.increased_endurance = increased_endurance
        self.ruggledness = ruggledness
        self.long_ears = long_ears

    def __str__(self):
        return "viviparous: %s, warm_blooded: %s, wool: %s, mammals: %s, increased_endurance: %s, ruggledness: %s, long_ears: %s" % (self.viviparous, self.warm_blooded, self.wool, self.mammals, self.increased_endurance, self.ruggledness, self.long_ears)