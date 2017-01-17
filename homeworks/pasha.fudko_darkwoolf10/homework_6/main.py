#!usr/bin/python3
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
import json

class Hero(object):
    def __init__(self, name, level, race):
        self.name = name
        self.level = level
        self.race = race
    def __json__(self):
        return {'name': self.name, 'level': self.level, 'race': self.race}

myHero = Hero("Alex", str(6), "ork")



with open("hero.json", 'w') as f:
        json.dump(myHero.__json__(), f)


root = Element('person')
tree = Element(root)
name = Element(myHero.name)
root.append(name)
name.text = myHero.name
root.set('id', 'name')
print etree.toString(root)
tree.write(open(r"index.xml", "w"))
