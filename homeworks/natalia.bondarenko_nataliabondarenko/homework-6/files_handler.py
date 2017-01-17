import json
import xml.etree.ElementTree as ET


class FilesHandler:

    
    def create_json_file(self, processed_object):
        data = json.dumps(processed_object, indent=4, separators=(',', ':'))
        file = open('results.json', 'w')
        file.write(data)
        file.close()

    def read_json_file(self, filename):
        file = open(filename, 'r')
        data = json.loads(file.read())
        print(data)
        file.close()
        
    def create_xml_file(self, processed_object):
        root = ET.Element('data')
        for keys in processed_object:
            child = ET.SubElement(root, keys)
            child.text = str(processed_object[keys])
        ET.dump(root)
        tree = ET.ElementTree(root)
        tree.write('results.xml')

    def read_xml_file(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        print(root.tag)
        for child in root:
            print(child.tag,'->', child.text)
    
