from Dinamik import Dinamik


class Studio(Dinamik):
    def __init__(self, amplifier, number_of_speakers, power, play_clean):
        Dinamik.__init__(self, amplifier, number_of_speakers, power, 'studio')
        self.play_clean = play_clean

    def clean_sound(self):
        return 'Clean sound Pro'