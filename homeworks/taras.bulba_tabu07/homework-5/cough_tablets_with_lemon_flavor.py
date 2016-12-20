from PillsMain import PillsMain

class CoughTabletsWithLemonFlavor(PillsMain):

    __lemon_flavor = 'lemon'

    def set_lemon_flawor(self, l):
        set.__lemon_flavor = 'lemon'

    def lemon_flavor(self):
        return self.__lemon_flavor

    def instruction_of_pills(self):
        super().instruction_of_pills()
        print('| P.S. This pills with' ,self.__lemon_flavor, 'flavor')

