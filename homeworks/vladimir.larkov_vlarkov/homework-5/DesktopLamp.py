from LightSource import LightSource


class DesktopLamp(LightSource):
    def __init__(self, color, size, lamp_type, price):
        self.color = color
        self.size = size
        self.lamp_type = lamp_type
        self.price = price

    def __str__(self):
        return "color - %s, size - %i cm, type - %s, price - % .2f $" % \
               (self.color, self.size, self.lamp_type, self.price)

    def turn_light_on(self):
        return "Desktop lamp - light is on"

    def turn_light_off(self):
        return "Desktop lamp - light is off"
