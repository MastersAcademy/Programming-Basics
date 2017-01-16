from Concert import Concert
from Home import Home
from Studio import Studio
import xml.etree.cElementTree as ET

info = open("info.json", "w")

concert1 = Concert('TD 2400', '4', '800', 'Play loud')
studio1 = Studio('TS 500', '3', '400', 'Play clear')
home1 = Home('sven 3s', '2', '50', 'Just play')

print(concert1)
print(studio1.pik_power())
print(home1.column_type)
print(studio1.clean_sound())


info.write(concert1.tojson())
info.close()

din = ET.Element("din")
characteristic = ET.SubElement(din, "characteristic")

ET.SubElement(characteristic, "field1", name="amplifier").text = home1.amplifier
ET.SubElement(characteristic, "field2", name="number_of_speakers").text = home1.number_of_speakers
ET.SubElement(characteristic, "field3", name="power").text = home1.power
ET.SubElement(characteristic, "field4", name="column_type").text = home1.column_type


tree = ET.ElementTree(din)
tree.write("filexml.xml")
