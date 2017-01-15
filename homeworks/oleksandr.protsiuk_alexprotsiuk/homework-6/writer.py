#  This file contain functions which used for creating JSON and XML files
import json
import xml.etree.cElementTree as Tree
full = {}


def writer(num, answ1, answ2, status):  # this fn is creating dict with attr.
    val = (answ1, answ2, status)
    full[num] = val


def write_to_json(k):  # this fn is writing dict created by "writer" in JSON-file
    with open('plain.json', 'w') as f:
        json.dump(k, f, indent=4)


def write_to_xml(num):  # this fn is writing dict created by "writer" in XML-file

    root = Tree.Element("root")

    for i in range(1, num+1):
        number = Tree.SubElement(root, "number", name=str(i))
        l = full[i]
        Tree.SubElement(number, "model").text = l[0]
        Tree.SubElement(number, "color").text = l[1]
        Tree.SubElement(number, "fuel").text = l[2]

    tree = Tree.ElementTree(root)
    tree.write("plain.xml")
