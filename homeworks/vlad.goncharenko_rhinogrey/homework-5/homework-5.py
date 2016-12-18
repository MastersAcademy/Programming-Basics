class Guitar:

    cathegory = 'string instrument'
    strings = 6
    using = 'used for playing music'

    def __init__(self):
        self.__string_construction = 'blabh blah blah blah'
        self.__tree_structure = 'blah baaalall blah'
        self.__assembling_process = '5$ in a day worker'

    def play(self):
        print('trrrrruuuuum!!')


class Acoustic_Guitar(Guitar):

    sound = 'acoustic construction'
    special_feature = 'can be used as an drum :D'

class Electric_Guitar(Guitar):

    sound = 'pickups and amplifier'
    special_feature = 'can be combined with various pedals and effects'

class Semi_Acoustic_Guitar(Guitar):

    sound = 'acoustic construction and microphone'

class Floyd_Rose_Guitar(Electric_Guitar):

    bridge_mechanism = 'floyd rose'


gtrEl = Electric_Guitar()
gtrEl.play()

