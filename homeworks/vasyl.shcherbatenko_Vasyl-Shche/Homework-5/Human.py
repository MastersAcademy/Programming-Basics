from Creature import Creature

class Human(Creature):
    def __init__(self, name, thing_property, gender, ability_to_die):
        Creature.__init__(self, name, thing_property, ability_to_die)
        self.gender = gender

    def __str__(self):
        print('Your name is %s,Can you think of?%s,what your gender %s,can your die %S' % (self.name, self.ability_to_die, self.gender, self.property_die))