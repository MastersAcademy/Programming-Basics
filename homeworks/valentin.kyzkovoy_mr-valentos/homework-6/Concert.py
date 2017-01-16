from Dinamik import Dinamik

class Concert(Dinamik):
    def __init__(self, amplifier, number_of_speakers, power, play_loud):
        Dinamik.__init__(self, amplifier, number_of_speakers, power, 'concert')
        self.play_loud = play_loud

    def loud_sound(self):
        return 'Very loud sound'