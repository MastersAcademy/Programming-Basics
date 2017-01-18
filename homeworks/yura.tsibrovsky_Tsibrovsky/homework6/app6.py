from Soundplaysystem import Soundplaysystem
from Mp3player import Mp3player
from Tapeplayer import Tapeplayer
import xml.etree.cElementTree as ET



datafile = open("datafile.json", "w")
mp3player_walkman = Mp3player('Sony Walkman', '2 W', 'AAA batteries', 'CD')
tapeplayer_vesna = Tapeplayer('Vesna', '5 W', '220 V', 'reel tape', 'volume control')

print(mp3player_walkman)
print(tapeplayer_vesna)

import json
def tojson(self):
    return json.dumps(self.__dict__, sort_keys=True, indent=4)

datafile.write(mp3player_walkman.tojson())
datafile.write(tapeplayer_vesna.tojson())
datafile.close()

din = ET.Element("din")
description = ET.SubElement(din, "description")

ET.SubElement(description, "field1", name="name").text = mp3player_walkman.name
ET.SubElement(description, "field2", name="input_source").text = mp3player_walkman.input_source
ET.SubElement(description, "field3", name="power_type").text = mp3player_walkman.power_type


ET.SubElement(description, "field4", name="name").text = tapeplayer_vesna.name
ET.SubElement(description, "field5", name="input_source").text = tapeplayer_vesna.input_source
ET.SubElement(description, "field6", name="power_type").text = tapeplayer_vesna.power_type


tree = ET.ElementTree(din)
tree.write("datafile.xml")
