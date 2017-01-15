from plain import Plain  # import Plain class


class MilPlain(Plain):  # class MilPlain is Plain class inheritance

    def __str__(self):
        return 'Ok! this is a military plane number %s and it is %s' % (self.number, self.color)
