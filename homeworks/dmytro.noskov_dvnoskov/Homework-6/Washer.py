class Washer():
    def __init__(self, water, power, loading, mode):
        self.water = water  # hot,cold
        self.power = power  # vat
        self.loading = loading  # kg
        self.mode = mode  # auto,manual


    def _power_run(self):
        return print('power equipment:%s \nencapsulation power equipment = 500 Vat' % (self.power))