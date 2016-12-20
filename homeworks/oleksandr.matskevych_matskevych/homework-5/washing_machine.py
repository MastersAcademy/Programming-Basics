
class washing_machine(object):
    def __init__(self, rpm, led_control, self_clean):
        self.rpm = rpm
        self.led_control = led_control
        self.self_clean = self_clean

    def __str__(self):
        return "washing machine, rpm: %s, led_control: %s, self_clean: %s " % (self.rpm, self.led_control, self.self_clean)

    def order_w_m(self):
        return "You order washing machine in stock"




