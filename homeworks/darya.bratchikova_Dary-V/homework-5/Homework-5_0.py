class Pen(object):
    def __init__(self, name, barcode, size, material):
        self.name = name
        self.barcode = barcode
        self.size = size
        self.material = material


        def __str__(self):
            return "name: %s, barcode: %s, size: %s, material: %s" % (self.name, self.barcode, self.size, self.material)

        def product(self):
            return "%s %s" % (self.name, self.barcode)