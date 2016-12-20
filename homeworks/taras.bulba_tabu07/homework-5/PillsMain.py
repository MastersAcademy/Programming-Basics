class PillsMain:

    __size = 0
    __weight = 0
    __form = 'n/a'

    def set_size(self, s):
        self.__size = s

    def set_weight(self, w):
        self.__weight = w

    def set_form(self, f):
        self.__form = f

    def instruction_of_pills(self):
        print('| ---Instruction---')
        print('| This pills weighs' ,self.__weight, 'grams')
        print('| Has the' ,self.__size, 'size')
        print('| And the form' ,self.__form,)
        print('| Use careful!')