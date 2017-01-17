import json
import xml.etree.ElementTree as etree
from Truck import Truck
from Automobile import Automobile

gaz = Truck(4, 3.3, 'asdf', 100)
print(gaz)

lanos = Automobile(4, 1.5, 'sedan', 5)
print(lanos)

print(gaz.drive())
print(lanos.drive())

with open('truck.json', 'w+') as outfile:
    json.dump(gaz.__dict__,  outfile, indent="")


xml_lanos = etree.Element("Automobile")
params = etree.SubElement(xml_lanos, "params")

etree.SubElement(params, "count_wheels").text = "4"
etree.SubElement(params, "engine").text = "1.5"
etree.SubElement(params, "body").text = "sedan"
etree.SubElement(params, "max_passengers").text = "5"

# xml_to_write = etree.ElementTree(xml_lanos)
# xml_to_write.write(open('lanos.xml', 'w+'))

# f =  open("myxmlfile.xml", "wb")
# f.write(etree.ElementTree(xml_lanos))
# f.close()

etree.ElementTree(xml_lanos).write('lanos.xml')