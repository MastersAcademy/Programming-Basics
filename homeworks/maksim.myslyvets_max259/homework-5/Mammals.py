class Mammals():
    def __init__(self, viviparous, warm_blooded, wool, mammals):
        self.viviparous = viviparous
        self.warm_blooded = warm_blooded
        self.wool = wool
        self.mammals = mammals

    def __str__(self):
        return "viviparous: %s, warm_blooded: %s, wool: %s, mammals: %s" % (self.viviparous, self.warm_blooded, self.wool, self.mammals)