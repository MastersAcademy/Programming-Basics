#!/usr/bin/env python3

from Vehicle import Vehicle
from Upgrade import Upgrade_car
from Paint import Paint


car1 = Upgrade_car("Audi", "Green")
car2 = Paint("Volga", "Red", "Brown")

print(car1.car_info())
print(car1.upgrade_motor()) 

print(car2.car_info())
print(car2.change_color())
