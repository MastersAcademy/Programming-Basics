import json
import xml.etree.ElementTree as ET


from Gun import Gun


Gun('Company', 'Model', 'fundation_year')
TTGun = {"Компанія": "Тульський завод", "Модель": "ТТ", "Рік заснування": "1930"}

outfile = open('saveJson.json', 'w')
json.dump(TTGun, outfile, indent=3, ensure_ascii=False)
outfile.close()

TTGun = ET.Element('TTGun')
feature = ET.SubElement(TTGun, 'feature')

ET.SubElement(feature, 'company', feature='company').text = "Tula plant"
ET.SubElement(feature, 'model', feature='model').text = "TT"
ET.SubElement(feature, 'fundation_year', feature='fundation_year').text = "1930"

tree = ET.ElementTree(TTGun)
tree.write('saveXml.xml')



