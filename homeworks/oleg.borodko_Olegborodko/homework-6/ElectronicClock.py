import time
from Clock import Clock

class ElectronicClock(Clock):
    __battery_stock = 100

    def __init__(self, size = "unknown", weight = "unknown", average_working_period = "unknown", material = "unknown", price = 100):
        Clock.__init__(self, size, weight, average_working_period)
        self.price = price
        print("New Electronic clock from %s" % material)

    def show_time(self):
        if self.__battery_stock >= 10:
            print("Time now - %s" % time.strftime("%X"))
            self.__battery_stock -= 10
            print("Battery stock = %s" % self.__battery_stock)
        else:
            print("You need to recharge clock")

    def recharge_clock(self):
        self.__battery_stock += 10
