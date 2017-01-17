import json
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree

root = Element('Creature')
tree = ElementTree(root)
name = Element('Name')
root.append(name)
name.text = 'Ivan'
ability_to_die = Element('Ability to die')
root.append(ability_to_die)
ability_to_die.text = 'True'
thing_property = Element('CPU')
root.append(thing_property)
thing_property.text = 'thing_property'
ram = Element('True')
print(etree.tostring(root))
tree.write(open('Creature.xml', 'wb'))


computer = {'Creature': {
                         'Name': 'Ivan',
                         'Ability to die': 'True',
                         'Thing prorerty ': 'true',
                         }}

string = json.dumps(computer, indent=4)
print(string)

file = open('Creature.json', 'w')
file.write(string)
file.close()