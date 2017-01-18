from Gun import Gun

class AsaultRifle(Gun):
    def __init__(self, name, caliber, barrel_length, type_of_reload, amount_of_ammo):
        Gun.__init__(self, name, caliber, barrel_length, type_of_reload, amount_of_ammo)


    def __shot(self, shots):
        if self.amount_of_ammo <= shots:
        	print('Need more ammo, reload a gun')
        else:
            self.amount_of_ammo -= shots
            print('Bang %i times' % (shots))	

