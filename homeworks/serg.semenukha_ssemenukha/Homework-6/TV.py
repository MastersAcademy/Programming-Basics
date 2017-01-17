import json
import xml.etree.ElementTree as ET

class BaseTV:
    def __init__(self, resolution, size):
        self.resolution = resolution
        self.size = size
        self.sources = ["hdmi", "dvi", "vga", "rf"]

    def scan(self):
        for source in self.sources:
            print("Scanning %s: no signal" % (source))

    def __str__(self):
        return "I'm basic TV having %s resolution and %d inches display size" % (self.resolution, self.size)

    def write_json(self):
        fp = open("json_%s_%s.json" % (self.size, self.resolution), "w")
        json.dump({
            "resolution": self.resolution,
            "size": self.size,
            "sources": self.sources,
            "description": self.__str__()
        }, fp)
        fp.close()

    def write_xml(self):
        # create root element
        document = ET.Element("tv")

        #create PARAMS node
        params = ET.SubElement(document, "params")
        ET.SubElement(params, "param", {"type": "resolution", "value": self.resolution})
        ET.SubElement(params, "param", {"type": "size", "value": str(self.size)})

        # create SOURCES node
        sources = ET.SubElement(document, "sources")
        for source in self.sources:
            ET.SubElement(sources, "source", {"value": source})

        # add some description
        ET.SubElement(document, "description").text = self.__str__()

        tree = ET.ElementTree(document)
        tree.write("xml_%s_%s.xml" % (self.size, self.resolution))
