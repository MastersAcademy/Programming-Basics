import json
import xml.etree.ElementTree as ETree
from Apple import Apple
from random import randint

class RedApple(Apple):
    def __init__(self, name, weight, last_day, price, can_discount):
        Apple.__init__(self, name, weight, last_day, 100)
        self.can_discount = can_discount

    def __set_discount(self):
        discount_value = randint(2, 20)

        price = self.price * self.weight

        price = int(price * (100 - discount_value) / 100)

        result = {
            'name': 'red apple',
            'discount': discount_value,
            'price': price,
            'weight': self.weight
        }
        print(result)

        #save file to json
        jsonF = open('JsonFile.json', 'w')
        json.dump(result, jsonF, indent=5)
        jsonF.close()


        #save file to xml
        shoplist = ETree.Element('shoplist')
        value = ETree.SubElement(shoplist, 'value')

        ETree.SubElement(value, 'name').text = 'red apple'
        ETree.SubElement(value, 'discount').text = 'from 2 to 20 percents'
        ETree.SubElement(value, 'price').text = '100'
        tree = ETree.ElementTree(shoplist)
        tree.write('XmlFile.xml')

        return result


    def __getPrice(self):
        if self.can_discount == 'true':
            data = self.__set_discount()
            return 'You are lucky, today you get discount \'%s\' percents and you needs pay \'%s\' dollars for \'%s\' kg instead of paying \'%s\' dollars. Have a nice day!' % (data['discount'], data['price'], self.weight, self.price)
        else:
            return 'You need pay \'%s\' dollars. Have a nice day!' % self.price
