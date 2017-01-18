import json
import dicttoxml
from brush import Brush
from xml.etree.ElementTree import Element, tostring

# Create some object
brushes = Brush("Colgate", "medium", "plastic")
# Convert to json and save to file
file_out_json = open('brush.json', 'w')
brushes_json = json.dump(brushes.__dict__, file_out_json, indent=4)
file_out_json.close()
# Convert to xml using an external module dicttoxml from https://pypi.python.org/pypi site
brushes_xml = dicttoxml.dicttoxml(brushes.__dict__, attr_type=False)
file_out_xml = open('brush.xml', 'wb')
file_out_xml.write(brushes_xml)
file_out_xml.close()


# Convert to xml using language features

def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


file_out_xml_2 = open('brush_1.xml', 'wb')
file_out_xml_2.write(tostring(dict_to_xml('brush', brushes.__dict__)))
file_out_xml_2.close()
