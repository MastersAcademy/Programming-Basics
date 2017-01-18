from computer import computer
from laptop import laptop
import json
import xml.etree.ElementTree as ET

voltage = int (input (" Input your voltage? "))
computer1 = computer('ARTLINE_Home_H43_v02','Win10','win_pc', voltage)
hp = laptop('HP_Pavilion_dv6-6c55er','Win10','laptop_pc', voltage)
print(computer1)
print(computer1.working())
print(hp)
print(hp.working())

# Homework-6

computer1_json = {
    "specifications": 'ARTLINE_Home_H43_v02',
    "software": 'Win10',
    "device_name": 'win_pc',
    "voltage": voltage,
}
s = json.dumps(computer1_json)

def transporter_in_json(self):
    z = open('computer1.json', 'w')
    z.write(self)
    z.close()

transporter_in_json(s)

hp_json = {
    "specifications": 'HP_Pavilion_dv6-6c55er',
    "software": 'Win10',
    "device_name": 'laptop_pc',
    "voltage": voltage,
}
s = json.dumps(hp_json)

def transporter_in_json(self):
    z = open('hp.json', 'w')
    z.write(self)
    z.close()

transporter_in_json(s)

def preobrazovatel_in_XML(self):
    dish = ET.Element('computer1')
    specifications = ET.SubElement(dish, 'specifications')
    specifications.text = self['specifications']
    software = ET.SubElement(dish, 'software')
    software.text = self['software']
    device_name = ET.SubElement(dish, 'device_name')
    device_name.text = self['device_name']
    tree = ET.ElementTree(dish)
    tree.write('computer1.xml')


perevod = preobrazovatel_in_XML(computer1_json)

