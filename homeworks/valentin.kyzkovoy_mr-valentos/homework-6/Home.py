from Dinamik import Dinamik


class Home(Dinamik):
    def __init__(self, amplifier, number_of_speakers, power, just_play):
        Dinamik.__init__(self, amplifier, number_of_speakers, power, 'home')
        self.jast_play = just_play

    def normal_sound(self):
        return 'Sound is OK'