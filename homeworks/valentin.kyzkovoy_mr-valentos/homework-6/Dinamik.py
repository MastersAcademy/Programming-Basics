import json
import xml.etree.cElementTree as ET

class Dinamik(object):
    def __init__(self, amplifier, number_of_speakers, power, column_type):
        self.amplifier = amplifier
        self.number_of_speakers = number_of_speakers
        self.power = power
        self.column_type = column_type

    def __str__(self):
            return "amplifier: %s, namber_of_speakers: %s, power: %s, column_type: %s" % \
                   (self.amplifier, self.number_of_speakers, self.power, self.column_type)

    def pik_power(self):
        return int(self.number_of_speakers) * int(self.power),'W'

    def tojson(self):
         return json.dumps(self.__dict__, sort_keys=True, indent=4)

    def toxml(self):

        din = ET.Element("din")
        characteristic = ET.SubElement(din, "characteristic")

        ET.SubElement(characteristic, "field1", name="amplifier").text = self.amplifier
        ET.SubElement(characteristic, "field2", name="number_of_speakers").text = self.number_of_speakers
        ET.SubElement(characteristic, "field3", name="power").text = self.power
        ET.SubElement(characteristic, "field4", name="column_type").text = self.column_type

        tree = ET.ElementTree(din)
        tree.write("filexml.xml")
