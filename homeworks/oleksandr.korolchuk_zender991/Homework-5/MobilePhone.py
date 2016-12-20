class MobilePhone:
    def __init__(self, brand, input_type):
        self.brand = brand
        self.input_type = input_type


    def __str__(self):
        return "brand %s" % self.brand