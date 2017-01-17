try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from washing_machine import washing_machine
wm = washing_machine('1000', 'color', 'yes')
print(wm.rpm)
wm = ET.Element("washing_machine")
characteristics = ET.SubElement(wm, "characteristics")

ET.SubElement(characteristics, "rpm", characteristic = "rpm").text = "rmp/min"
ET.SubElement(characteristics, "led_control", characteristic = "led_control").text = "color or monochrome led control"
ET.SubElement (characteristics, "self_clean", characteristic = "self_clean"). text = "self clean yes or not"

tree = ET.ElementTree(wm)
tree.write("homework6.xml")