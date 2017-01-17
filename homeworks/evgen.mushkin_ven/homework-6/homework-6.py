import json
import dicttoxml
from SpoonBait import SpoonBait

spoonBait = SpoonBait('white', '70%', '12g')
print(spoonBait.color)
print(spoonBait.catch)
print(spoonBait.proportions)

with open('object.json', 'w') as o:
    json.dump(spoonBait.__dict__, o, indent=4)

with open('object.xml', 'wb+') as o:
    o.write(dicttoxml.dicttoxml(spoonBait.__dict__))
