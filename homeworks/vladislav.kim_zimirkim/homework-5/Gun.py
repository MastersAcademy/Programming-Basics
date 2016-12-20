class Gun(object):
    def __init__(self, name, caliber, barrel_length, type_of_reload, amount_of_ammo):
        self.name = name
        self.caliber = caliber
        self.barrel_length = barrel_length
        self.type_of_reload = type_of_reload
        self.amount_of_ammo = amount_of_ammo
    
    

    def __str__(self):
        return "name: %s,\n caliber: %f,\n barel_length: %f,\n type_of_reload: %s,\n amount_of_ammo: %i \n" % (self.name, self.caliber, self.barrel_length, self.type_of_reload, self.amount_of_ammo)
    def check_ammo(self):
        print ("name: %s, amount of ammo: %i \n" % (self.name,self.amount_of_ammo))

    def shot(self):
        if self.amount_of_ammo <= 0:
            print('No ammo, reload a gun')
        else:
            self.amount_of_ammo -= 1
            print('Bang!')
    