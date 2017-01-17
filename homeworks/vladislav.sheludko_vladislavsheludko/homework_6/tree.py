try:
    import xml.etree.cElementTree as Tree
except ImportError:
    import xml.etree.ElementTree as Tree
from Car import Car
mycar = Car('Black', '12 L/60 mph', '350 h.m.', '6', '120 mph')
mycar = Tree.Element("MyCar")
technical = Tree.SubElement(mycar, "technical")

Tree.SubElement(technical, "Color").text = "The color of car"
Tree.SubElement(technical, "Petrol").text = "Fuel consumption"
Tree.SubElement (technical, "Engine"). text = "Engine power"
Tree.SubElement (technical, "Gear_box"). text = "Quantity of gears"
Tree.SubElement(technical, "Speed").text = "The max speed"

tree = Tree.ElementTree(mycar)
tree.write(open("home_6.xml", 'wb'))

