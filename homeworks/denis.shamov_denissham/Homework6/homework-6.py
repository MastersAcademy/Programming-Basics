import json

import xml.etree.cElementTree as ET

from Vehicle import Vehicle

from Car import Car

from Cargo_car import Cargo_car

Car1 = Car('4', 'Cherkassy', 'Kiev', 'Petrol engine', 'true')

Cargo_car1 = Cargo_car('4', 'Cherkassy', 'Tbilisi', 'Petrol engine', 'true')

file_json = open("Cars.json", "w")
json.dump({"Car1": Car1.__dict__, "Cargo_car1": Cargo_car1.__dict__}, file_json, indent=4)
file_json.close()

root = ET.Element("Vehicle")
small_car = ET.SubElement(root, "Car")
big_car = ET.SubElement(root, "Cargo_car")

for k, item in Car1.__dict__.items():
    ET.SubElement(small_car, k).text = str(item)

for k, item in Cargo_car1.__dict__.items():
    ET.SubElement(big_car, k).text = str(item)

tree = ET.ElementTree(root)
tree.write("Cars.xml")