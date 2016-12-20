class Soundplaysystem(object):
    def __init__(self, name, output_power, power_type, input_source, turn_type):
        self.name = name
        self.output_power = output_power
        self.power_type = power_type
        self.input_source = input_source
        self.turn_type = turn_type

    def __str__(self):
        return "name: %s, output_power: %s, power_type: %s, input_source: %s, turn_type: %s" % (self.name, self.output_power, self.power_type, self.input_source, self.turn_type)

    def general_name(self):
        return "%s %s" % (self.input_source, self.name)


