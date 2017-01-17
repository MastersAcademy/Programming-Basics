#!/usr/bin/env python3

from Vehicle import Vehicle
from Upgrade import UpgradeCar
from Paint import Paint
from convert import *


car1 = UpgradeCar("Audi", "Green")
car2 = Paint("Volga", "Red", "Brown")

print(car1.car_info())
print(car1.upgrade_motor()) 

print(car2.car_info())
print(car2.change_color())

#homework-6
# convert to json file
to_json(car1)
# convert to xml file
to_xml(car2)
print("object added on files")