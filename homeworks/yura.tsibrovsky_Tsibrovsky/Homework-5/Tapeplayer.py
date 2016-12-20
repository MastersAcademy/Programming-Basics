from Soundplaysystem import Soundplaysystem


class Tapeplayer(Soundplaysystem):
    def __init__(self, name, output_power, power_type, input_source, turn_type):
        Soundplaysystem.__init__(self, name, output_power, power_type, input_source, turn_type)



vesna1 = Tapeplayer('Vesna1', '5 W', '220 V', 'reel tape', 'volume control')
print(vesna1)