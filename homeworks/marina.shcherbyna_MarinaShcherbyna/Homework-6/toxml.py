#!/usr/bin/env python3
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from classes5 import Human
girl = Human('green', 'blond', '60', '175')
print (girl.eye_colour)
girl = ET.Element("girl")
characteristics = ET.SubElement(girl, "characteristics")

ET.SubElement(characteristics, "eye_colour", characteristic = "eye_colour").text = "The colour of eyes"
ET.SubElement(characteristics, "hair_colour", characteristic = "hair_colour").text = "The native hair colour"
ET.SubElement (characteristics, "weight", characteristic = "weight"). text = "Kilograms amount of the body"
ET.SubElement (characteristics, "height", characteristic = "height"). text = "Metres amount of the body"

tree = ET.ElementTree(girl)
tree.write("homework6.xml")
