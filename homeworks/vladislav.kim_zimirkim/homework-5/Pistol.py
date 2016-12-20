from Gun import Gun

class Pistol(Gun):
    def __init__(self,name, caliber, barrel_length, type_of_reload, amount_of_ammo, type_of_ammo):
        Gun.__init__(self, name, caliber, barrel_length, type_of_reload, amount_of_ammo)
        self.type_of_ammo = type_of_ammo


    def __str__(self):
        return "name: %s,\n caliber: %f,\n barel length: %f,\n type of reload: %s,\n amount of ammo: %i,\n type of ammo: %s \n" % (self.name, self.caliber, self.barrel_length, self.type_of_reload, self.amount_of_ammo, self.type_of_ammo)    


 


