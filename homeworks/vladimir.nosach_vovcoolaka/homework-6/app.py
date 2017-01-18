import json
import xml.etree.ElementTree as ET

from Door import Door
from ArmoredDoor import ArmoredDoor


door1 = Door("Berez", 85, 210, "Brown", 4515)
door2 = Door("Berez", 95, 200, "White", 4815)
door3 = ArmoredDoor("Straj", 105, 200, "Black", 6545, "Cylindrical")

door1.description_of_door()
door2.description_of_door()
door3.description_of_door()


write_json_file = open('doors.json', 'w')
doors_json1 = json.dump(door1.__dict__, write_json_file, indent=4)
#doors_json2 = json.dump(door2.__dict__, write_json_file, indent=4)#
#doors_json3 = json.dump(door3.__dict__, write_json_file, indent=4)#
write_json_file.close()



root = ET.Element("doors")
doc = ET.SubElement(root, "door1")

ET.SubElement(doc, "model", name="berez")
ET.SubElement(doc, "width", name="85")
ET.SubElement(doc, "lenght", name="210")
ET.SubElement(doc, "colour", name="Brown")
ET.SubElement(doc, "Number", name="4515")

tree = ET.ElementTree(root)
tree.write("doors.xml")