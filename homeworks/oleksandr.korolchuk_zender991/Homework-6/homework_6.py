from faker import Factory as FakerFaktory
import json
import xml.etree.ElementTree as ET

faker = FakerFaktory.create()

class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


person1 = Person(faker.first_name(), faker.last_name(), faker.email())
person2 = Person(faker.first_name(), faker.last_name(), faker.email())

persons = [person1, person2]   # list of created persons

#----------======== Conver To JSON ==========------------

def convertToJSON(self):   # method for convertation from object to JSON
    return json.dumps(self.__dict__, sort_keys=True, indent=4)

people = open('result.json', 'a')

for each_person in persons:   # convert each objects from list to JSON and write to the file
    object_in_json = convertToJSON(each_person)
    people.write(object_in_json)

people.close
#----------======== Conver To JSON ==========------------

#----------======== Conver To XML ==========------------

root = ET.Element('people')   # create XML tree
tree = ET.ElementTree(root)


for each_person in persons:   # select each person in list

    current_person = each_person.__dict__   # convert to dictionary type

    person = ET.Element('person')   # create head element for each person
    root.append(person)     # add element to the tree

    for k,v in current_person.items():   # select person

        k = ET.Element('%s' % k)    # use person's key from dictionary for create tag in XML tree
        person.append(k)    # add tag to the tree
        k.text = v   # use persons's value from dictionary for create text between tags


tree = ET.ElementTree(root)
tree.write("result2.xml")   # write XML tree to the file

#----------======== Conver To XML ==========------------