from MobilePhone import MobilePhone

#let's imagine that all buttons phones can't connect to the internet
class ButtonMobilePhone(MobilePhone):
    def __init__(self, input_type, brand):
        MobilePhone.__init__(self, brand, input_type)

    def __str__(self):
        return "Type: %s, brand %s" % (self.input_type, self.brand)

    def make_call(self):
        return 'In phone ' + self.brand + ' you should press buttons for call'

    def connect_to_internet(self):
        return "Your phone hasn't internet connection"

    def beat_nuts(self):
        return "Your nut is splited"