import json
import dicttoxml
from SpoonBait import SpoonBait


def create_files(obj):
    with open('object.json', 'w') as o:
        json.dump(obj.__dict__, o, indent=4)

    with open('object.xml', 'wb+') as o:
        o.write(dicttoxml.dicttoxml(obj.__dict__))


spoonBait = SpoonBait('white', '70%', '12g')
print(spoonBait.__dict__)

create_files(spoonBait)
