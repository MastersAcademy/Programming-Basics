import json
import xml.etree.cElementTree as ET
from Classes import Television, Smart

smart_tv = Smart("some_format", "some_format", "signal_type", 30, False, True)
old_tv = Television("some_format", "some_format", "signal_type", 30)
# -----------------Making JSON file-------------------------- #
fileJSON = open("fileJ.json", "w")
json.dump({"smart_tv": smart_tv.__dict__, "old_tv": old_tv.__dict__}, fileJSON, indent=4)
fileJSON.close()

# -----------------Making XML file----------------------------- #
root = ET.Element("Television")
newer = ET.SubElement(root, "smart_tv")
elder = ET.SubElement(root, "elder_tv")

for key, item in smart_tv.__dict__.items():
    ET.SubElement(newer, key).text = str(item)

for key, item in old_tv.__dict__.items():
    ET.SubElement(elder, key).text = str(item)

tree = ET.ElementTree(root)
tree.write("fileX.xml")
