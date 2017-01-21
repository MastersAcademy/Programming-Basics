from Coffee import Coffee


class CoffeeWithMilk(Coffee):
    def __init__(self, beans, water, milk):
        Coffee.__init__(self, beans, water)
        self.milk = milk

    def __str__(self):
        return "beans: %s, water: %s, milk: %s" %(self.beans, self.water, self.milk)

