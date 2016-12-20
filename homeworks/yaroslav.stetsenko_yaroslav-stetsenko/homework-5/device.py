class device(object):
    def __init__(self, specifications, software, computer_name, voltage):
        self.specifications = specifications
        self.software = software
        self.device_name = computer_name
        self.voltage = voltage

    def __str__(self):
        return "specifications: %s, software: %s, device_name: %s, voltage: %s" % (self.specifications, self.software, self.device_name, self.voltage)

    def full_name(self):
        return "%s %s" % (self.specifications, self.device_name)

