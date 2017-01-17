from DesktopLamp import DesktopLamp


class SmartDesktopLamp(DesktopLamp):
    __wifi_module_initialization = True  # private variable

    def __init__(self, color, size, price, can_connect_to_network, can_exchange_data):
        DesktopLamp.__init__(self, color, size, "smart lamp", price)
        self.can_connect_to_network = can_connect_to_network
        self.can_exchange_data = can_exchange_data

    def __str__(self):
        return super().__str__() + ", can connect to the network - %r, can exchange data - %r" % \
                                   (self.can_connect_to_network, self.can_exchange_data)

    def connect_to_network(self):
        if self.__wifi_module_initialization:
            return "Connected to network."
        else:
            return "Connection failed. Please check WiFi module."

    def exchange_data(self):
        return self.connect_to_network() + " Can exchange data."

    def turn_light_on(self):  # method overrode/expanded
        return "Smart desktop lamp - light is on"

    def turn_light_off(self):  # method overrode/expanded
        return "Smart desktop lamp - light is off"
