from Creature import Creature

class God(Creature):
    def __init__(self, thing_property,  ability_to_die, biuld_property):
        Creature.__init__(self, 'God', thing_property,  ability_to_die)
        self.biuld_property = biuld_property



    def creation(self):
          print('God is create world')

    def description_of_god(self):
        print("======================")
        print(" He is ", self.name())
        print(" Can it think? ", self.thing_property())
        print(" Can Die? ", self.ability_to_die())
        print(" Can build ", self.biuld_property)


