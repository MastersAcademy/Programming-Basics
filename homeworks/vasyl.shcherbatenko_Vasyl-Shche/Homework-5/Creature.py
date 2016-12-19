class Creature:
    def __init__(self,name,thing_property,property_die):
        self.name=name
        self.thing_property=thing_property
        self.property_die=property_die

        def __str__(self):
            return 'Name is %s ability to think %s Can you die %s' %(self.name,self.thing_property,self.property_die)