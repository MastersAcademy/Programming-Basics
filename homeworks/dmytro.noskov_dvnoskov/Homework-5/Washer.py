class Washer():
    def __init__(self, water, power, loading, mode):
        self.water = water  # hot,cold
        self.power = power  # vat
        self.loading = loading  # kg
        self.mode = mode  # auto,manual


    def power_run(self):
        return print('power equipment:%s \n encapsulation power equipment = 500 Vat' % (self.power))
