class Washer():
    def __init__(self, water,power,loading,mode):
        self.water = water  #hot,cold
        self.power = power   #vat
        self.loading = loading   # kg
        self.mode = mode    # auto,manual
#    def __str__(self):
 #       return "water: %s, power: %s, loading:%s, mode: %s" %(self.water,self.power,self.loading,self.mode)
    def power_work(self):
        print( 'power equipment:%s \n encapsulation power equipment = 500 Vat' % (self.power))




