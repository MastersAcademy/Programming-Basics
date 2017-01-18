import json
import xml.etree.ElementTree as ET
from Glasses import Glasses


class SunGlasses(Glasses):
    def __init__(self, model, frame, lens, shape, light_transmission, color):
        super().__init__(frame, lens, shape)
        self.model = model
        self.light_transmission = light_transmission
        self.color = color

    def __str__(self):
        return "Sunglasses Model: %s\n Frame: %s\n Lens: %s\n Shape: %s\n Light: %s\n Color: %s" \
               % (self.model, self.frame, self.lens, self.shape, self.light_transmission, self.color)

    def convert_to_json(self):
        dict_file = {"model": self.model, "frame": self.frame, "lens": self.lens, "shape": self.shape,
                     "light_transmission": self.light_transmission, "color": self.color}
        json_file = json.dumps(dict_file, indent=4)
        return json_file

    def convert_to_xml(self):
        sunglasses = ET.Element("sunglasses")
        details = ET.SubElement(sunglasses, "details")

        ET.SubElement(details, "model").text = self.model
        ET.SubElement(details, "frame").text = self.frame
        ET.SubElement(details, "lens").text = self.lens
        ET.SubElement(details, "shape").text = self.shape
        ET.SubElement(details, "light_transmission").text = self.light_transmission
        ET.SubElement(details, "color").text = self.color

        xml_file = ET.ElementTree(sunglasses)
        return xml_file

    def save_to_file(self, data):
        if data.__class__ == str:
            file = open(self.model + ".json", "w")
            file.write(data)
            file.close()
        elif data.__class__ == ET.ElementTree:
            data.write(self.model + ".xml")
        else:
            print("Wrong file type!")
