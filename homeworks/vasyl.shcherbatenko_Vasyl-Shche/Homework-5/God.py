from Creature import Creature

class God(Creature):
    def __init__(self,name,thing_property, property_die,biuld_property):
        Creature.__init__(self,name,thing_property,property_die)
        self.biuld_property=biuld_property


        def creation(self):
          print('God is create world')


