from device import device


class computer(device):
    def __init__(self, specifications, software, device_name, voltage):
        device.__init__(self, specifications, software, device_name, voltage)

    def working(self):
        if self.voltage in range(200, 240):
            print("You computer is working ")
        elif self.voltage < 200:
            print("You computer is not working")
        else:
            self.voltage  >= 241
            print('Error')

