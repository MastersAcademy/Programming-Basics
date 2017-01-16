import json

class Dinamik(object):
    def __init__(self, amplifier, number_of_speakers, power, column_type):
        self.amplifier = amplifier
        self.number_of_speakers = number_of_speakers
        self.power = power
        self.column_type = column_type

    def __str__(self):
            return "amplifier: %s, namber_of_speakers: %s, power: %s, column_type: %s" % \
                   (self.amplifier, self.number_of_speakers, self.power, self.column_type)

    def pik_power(self):
        return int(self.number_of_speakers) * int(self.power),'W'

    def tojson(self):
         return json.dumps(self.__dict__, sort_keys=True, indent=4)
