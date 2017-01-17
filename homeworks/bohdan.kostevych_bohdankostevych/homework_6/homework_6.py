import json
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree

root = Element('PC')
tree = ElementTree(root)
name = Element('Name')
root.append(name)
name.text = 'Asus'
model = Element('Model')
root.append(model)
model.text = 'R510VX'
cpu = Element('CPU')
root.append(cpu)
cpu.text = 'Intel'
ram = Element('RAM')
root.append(ram)
ram.text = '2 GB'
print(etree.tostring(root))
tree.write(open('computer.xml', 'wb'))


computer = {'PC': {
    'Name': 'Asus',
    'Model': 'R510VX',
    'CPU': 'Intel',
    'RAM': '2 GB'
}}

string = json.dumps(computer)
print(string)

file = open('computer.json', 'w')
file.write(string)
file.close()
