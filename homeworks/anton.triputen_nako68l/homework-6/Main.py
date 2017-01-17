from Salad import *
from Salad2 import *
import json
import xml.etree.ElementTree as ET

tst1 = Salad('tomato', 'cucumber', 'latuk', 'raisins')
print(tst1)
print(tst1.thought())

tst2 = Salad2('tomato', 'cucumber', 'arugula', 'kale', 'mayou')
print(tst2)
print(tst2.thought_about_second_salat())

# Homework-6 task
salat1_json = {
    "ingredient1": 'tomato',
    "ingredient2": 'cucumber',
    "ingredient3": 'latuk',
    "ingredient4": 'raisins',
}
s = json.dumps(salat1_json)


def transporter_in_json(self):
    z = open('file_2.json', 'w')
    z.write(self)
    z.close()


transporter_in_json(s)


def preobrazovatel_in_XML(self):
    dish = ET.Element('Salat')
    ingredient1 = ET.SubElement(dish, 'ingredient1')
    ingredient1.text = self['ingredient1']
    ingredient2 = ET.SubElement(dish, 'ingredient2')
    ingredient2.text = self['ingredient2']
    ingredient3 = ET.SubElement(dish, 'ingredient3')
    ingredient3.text = self['ingredient3']
    ingredient4 = ET.SubElement(dish, 'ingredient4')
    ingredient4.text = self['ingredient4']
    tree = ET.ElementTree(dish)
    tree.write('file_3.xml')


perevod = preobrazovatel_in_XML(salat1_json)