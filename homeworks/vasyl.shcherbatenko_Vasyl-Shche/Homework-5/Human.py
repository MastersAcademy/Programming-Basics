from Creature import Creature

class Human(Creature):
    def __init__(self,name,thing_property,gender,property_die):
        Creature.__init__(self,name,thing_property,property_die)
        self.gender=gender

