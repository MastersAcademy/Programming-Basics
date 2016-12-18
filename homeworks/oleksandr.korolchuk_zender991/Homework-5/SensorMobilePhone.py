from MobilePhone import MobilePhone

class SensorMobilePhone(MobilePhone):
    def __init__(self, input_type, brand):
        MobilePhone.__init__(self, brand, input_type)

    def __str__(self):
        return "Type: %s, brand %s" % (self.input_type, self.brand)

    def make_call(self):
        return 'In phone ' + self.brand + ' you should tap screen for call'

    def connect_to_internet(self):
        return "Connected successfully"