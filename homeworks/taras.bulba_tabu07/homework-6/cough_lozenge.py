from PillsMain import PillsMain
from cough_tablets_with_lemon_flavor import CoughTabletsWithLemonFlavor
import json
import dicttoxml

filename = 'data.json'
myFile = open(filename, mode='w')

cough_lozenge1 = PillsMain()
cough_lozenge2 = CoughTabletsWithLemonFlavor()

cough_lozenge1.set_weight(150)
cough_lozenge1.set_size(70)
cough_lozenge1.set_form('ring')
cough_lozenge1.instruction_of_pills()

cough_lozenge2.set_weight(300)
cough_lozenge2.set_size(150)
cough_lozenge2.set_form('oval')
cough_lozenge2.instruction_of_pills()

cough_lozenge1_dict = {
    'weight': cough_lozenge1.set_weight(150),
    'size': cough_lozenge1.set_size(70),
    'form': cough_lozenge1.set_form('ring')
}

cough_lozenge2_dict = {
    'weight': cough_lozenge2.set_weight(300),
    'size': cough_lozenge2.set_size(150),
    'form': cough_lozenge2.set_form('oval')
}

cough_lozenge = []
cough_lozenge.append(cough_lozenge1_dict)
cough_lozenge.append(cough_lozenge2_dict)

json.dump(cough_lozenge, myFile)
myFile.close()

xml = dicttoxml.dicttoxml(cough_lozenge1_dict, cough_lozenge2_dict)
filename="data.xml"
f = open(filename,'wb+')
f.write(xml)
f.close