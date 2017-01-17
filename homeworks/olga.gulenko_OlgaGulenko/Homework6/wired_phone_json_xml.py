import json
try:
    import xml.etree.ElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from Wired_phone import WiredPhone

phone = WiredPhone('Color: red','Model: A76','Inventory number: 12','Appointment: accounts department')
resultJson = {"color":"red", "model":"A76", "inventory_number":"12", "appointment":"accounts department"}
print(resultJson)

phone = ET.Element('phone')
attributes = ET.SubElement(phone, 'attributes')
ET.SubElement (attributes,'color', attribut ='color').text = 'Color: red'
ET.SubElement (attributes,'model', attribut ='model').text = 'Model: A76'
ET.SubElement (attributes,'inventory_number', attribut ='inventory_number').text = 'Inventory number: 12'
ET.SubElement (attributes,'appointment', attribut ='appointment').text = 'Appointment: accounts department'

file = open('data.json','w')
json.dump(resultJson, file)
file.close()

resultXml = ET.ElementTree(phone)
resultXml.write('data.xml')