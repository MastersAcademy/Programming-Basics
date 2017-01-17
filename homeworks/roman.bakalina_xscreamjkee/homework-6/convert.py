#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import json


def to_xml(self):
	root = ET.Element("xml")
	car = ET.SubElement(root, "car") 
	for key, item in self.__dict__.items():
		ET.SubElement(car, key).text = str(item)
	tree = ET.ElementTree(root)
	tree.write("file.xml")

def to_json(self):
	with open('file.json', 'w') as f:
		json.dump(self.__dict__, f, indent=4)

