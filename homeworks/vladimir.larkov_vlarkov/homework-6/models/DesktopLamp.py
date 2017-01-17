import json
import xml.etree.cElementTree as eTree
from LightSource import LightSource


class DesktopLamp(LightSource):
    def __init__(self, color, size, lamp_type, price):
        self.color = color
        self.size = size
        self.lamp_type = lamp_type
        self.price = price

    def __str__(self):
        return "color - %s, size - %i cm, type - %s, price - % .2f $" % \
               (self.color, self.size, self.lamp_type, self.price)

    def turn_light_on(self):
        return "Desktop lamp - light is on"

    def turn_light_off(self):
        return "Desktop lamp - light is off"

    # encode object into json file
    def encode_json(self):
        json_string = json.dumps(self.__dict__, indent=4, separators=(',', ':'))
        f = open("desktop_lamp.json", "w")
        f.write(json_string + '\n')
        f.close()

        print("Encoded to json successfully!")

    # encode object into xml file
    def encode_xml(self):
        root = eTree.Element("desktop_lamp")
        properties = eTree.SubElement(root, "properties")
        eTree.SubElement(properties, "property", name="color").text = self.color
        eTree.SubElement(properties, "property", name="size").text = str(self.size)
        eTree.SubElement(properties, "property", name="type").text = self.lamp_type
        eTree.SubElement(properties, "property", name="price").text = str(self.price)
        tree = eTree.ElementTree(root)
        tree.write("desktop_lamp.xml", encoding="utf-8", xml_declaration=True)

        print("Encoded to xml successfully!")
