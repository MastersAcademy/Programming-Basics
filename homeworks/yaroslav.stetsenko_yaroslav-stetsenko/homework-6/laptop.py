from device import device

class laptop(device):
    def __init__(self, specifications, software, device_name, voltage):
        device.__init__(self, specifications, software, device_name, voltage)


    def working(self):
        if self.voltage in range(100, 240):
            print("You laptop is working from the network")
        elif self.voltage < 100:
            print("You laptop is working from the battery")
        else:
            self.voltage  >= 241
            print('Error')