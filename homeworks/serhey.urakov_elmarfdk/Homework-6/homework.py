import json
import xml.etree.ElementTree as ET


class Terminator:
    def __init__(self, model, power_source, firearms, skin):
        self.model = model
        self.power_source = power_source
        self.firearms = firearms
        self.skin = skin

    def __str__(self):
        return "model: %s, power_source: %s, firearms: %s, skin: %s" % (self.model, self.power_source, self.firearms,
                                                                        self.skin)


arnold = Terminator('T850', 'mini reactor', 'different handguns', 'organic camouflage')
term = [arnold]


def convj(self):
    return json.dumps(self.__dict__, sort_keys=True, indent=4)


people = open('ter4.json', 'a')

for allTerm in term:
    object_in_json = convj(allTerm)
    people.write(object_in_json)

arnold = ET.Element('arnold')
param = ET.SubElement(arnold, 'param')
ET.SubElement(param, 'model', attribut='model').text = 'T850'
ET.SubElement(param, 'power_source', attribut='power_source').text = 'mini reactor'
ET.SubElement(param, 'firearms', attribut='firearms').text = 'different handguns'
ET.SubElement(param, 'skin', attribut='skin').text = 'organic camouflage'

resultXml = ET.ElementTree(arnold)
resultXml.write('ter4.xml')
