import json
import xml.etree.ElementTree as ET

from Blender import Blender

Blender1=Blender('Braun', '800', 'red', 'steal', '30', '2')

Blender1.description_of_Blender()

write_json_file = open('Blender1.json', 'w')
doors_json1 = json.dump(Blender1.__dict__, write_json_file, indent=4)

write_json_file.close()

root = ET.Element("Blender")
doc = ET.SubElement(root, "Blender1")

ET.SubElement(doc, "brand", name="Braun")
ET.SubElement(doc, "wattage", name="800")
ET.SubElement(doc, "color", name="red")
ET.SubElement(doc, "material", name="steal")
ET.SubElement(doc, "size", name="30")
ET.SubElement(doc, "weight", name="2")

tree = ET.ElementTree(root)
tree.write("Blender.xml")