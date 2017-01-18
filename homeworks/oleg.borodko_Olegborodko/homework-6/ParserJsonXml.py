import json
from dicttoxml import dicttoxml

class ParserJsonXml(object):
    def __init__(self, object):
        self.class_name = object.__class__.__name__
        self.object = object.__dict__

    def parser_json(self):
        return json.dumps(self.object)

    def parser_xml(self):
        return dicttoxml(self.object, custom_root=self.class_name, attr_type=False, root=False)

