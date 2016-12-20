from washing_machine import washing_machine

class washing_machine_smart(washing_machine):
    def __init__(self, model, rpm, led_control, self_clean, smart, energy):
        washing_machine.__init__(rpm, led_control, self_clean)
        self.smart = smart
        self.energy = energy
        self.model = model

    def __str__(self):
        return "Smart washing machine, model: %s, rpm: %s, led_control: %s, self_clean: %s smart: %s energy: %s " % (self.model, self.rpm, self.led_control, self.self_clean, self.energy)

    def order_w_m_s(self):
        return "You order smart washing machine in stock"


