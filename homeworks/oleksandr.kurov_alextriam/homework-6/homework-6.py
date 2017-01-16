print("We fly on a plane")
trapdoor = input("Trapdoor open or close? ")
fuel= input ("Type fuel level - full or low ")
weight= int (input ("Type weight your plane "))

from airplane import airplane
boing = airplane (trapdoor,fuel,weight)
print (boing.takeoff())

# save to json
import json
with open('json.txt', 'w+') as outfile:
    json.dump(boing.__dict__,  outfile, indent="")

#save to xml
import dicttoxml
xml = dicttoxml.dicttoxml(boing.__dict__)
filename="object.xml"
f = open(filename,'wb+')
f.write(xml)
f.close
