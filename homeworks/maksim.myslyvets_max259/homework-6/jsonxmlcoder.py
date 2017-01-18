import json
import dicttoxml


#представляємо об'єкти класу Mammals в якості словників для подальшого перетворення

dictCow = {"viviparous": "viviparous", "warm_blooded": "warm_blooded", "wool": "wool", "mammals": "mammals", "increased_endurance": "giving_meat", "ruggledness": "geaving_milk"}
dictDonkey = {"viviparous": "viviparous", "warm_blooded": "warm_blooded", "wool": "wool", "mammals": "mammals", "increased_endurance" : "increased_endurance", "ruggledness" : "ruggledness", "long_ears" : "long_ears"}
dictHorse = {"viviparous": "viviparous", "warm_blooded": "warm_blooded", "wool": "wool", "mammals": "mammals", "increased_endurance": "race", "ruggledness": "carry_things"}


with open('object.json', 'w') as o:
    json.dump(dictCow, o, indent=4)
    json.dump(dictDonkey, o, indent=4)
    json.dump(dictHorse, o, indent=4)



xml1 = dicttoxml.dicttoxml(dictCow)
xml2 = dicttoxml.dicttoxml(dictDonkey)
xml3 = dicttoxml.dicttoxml(dictCow)

f = open('object.xml','wb+')
f.write(xml1)
f.write(xml2)
f.write(xml3)
f.close()

