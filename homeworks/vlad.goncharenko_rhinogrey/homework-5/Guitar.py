class Guitar:

    cathegory = 'string instrument'
    strings = 6
    using = 'used for playing music'

    def __init__(self):
        self.__sound = 'trrruuuuummmm!!!!'

    def play(self):
        print(self.__sound)
