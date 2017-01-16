from MobileTelephone import MobilePhone
import json
import xml.etree.ElementTree as etree



class IphoneFourS(MobilePhone):
    def __init__(self, model, version, screen, width, height, the_weight, camera, video_resolution):
        MobilePhone.__init__(self, model, version, screen, width, height, the_weight, camera)
        self.video_resolution = video_resolution

        def __str__(self):
            return 'model: %s, version: %s, screen: %s, width: %s, height: %s, the weight: %s, camera: %s, video_resolution: %s' % (
                self.model, self.version, self.screen, self.width, self.height, self.the_weight, self.camera,
                self.video_resolution)


obj = IphoneFourS('4s', '5', '3.8', '130mm', '20mm', '25mm', '8px', 'HD')

# -------------------------------------- ====== JSON ====== --------------------------------------------


# fileName = 'iphone4s.json'

# accessMode = 'w'

# mobile_4s = json.dumps(obj.__dict__, indent=4, sort_keys=True)

# myFile = open(fileName, accessMode)
# myFile.write(mobile_4s)
# myFile.close()


fileName = 'iphone4s.json'

accessMode = 'w'

def mobile(self):

    return json.dumps(self.__dict__, indent=4, sort_keys=True)

mobile_4s = mobile(obj)

myFile = open(fileName, accessMode)
myFile.write(mobile_4s)
myFile.close()


# -------------------------------------- ====== XML ====== ----------------------------------------------

obj2 = obj.__dict__

def add_items(root, items):

    for name, text in items:
        elem = etree.SubElement(root, name)
        elem.text = text

root = etree.Element('Mobile')
add_items(etree.SubElement(root, 'Iphone4s'),
          ((key.replace('',''), value) for key, value in obj2.items()))

tree = etree.ElementTree(root)
tree.write('iphone4s.xml', xml_declaration=True, encoding='utf-8')








