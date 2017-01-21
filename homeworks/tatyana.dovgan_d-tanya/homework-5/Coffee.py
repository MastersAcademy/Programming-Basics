class Coffee():
    def __init__(self, beans, water):
        self.beans = beans
        self.water = water

    def __str__(self):
        return "beans: %s, water: %s" %(self.beans, self.water)