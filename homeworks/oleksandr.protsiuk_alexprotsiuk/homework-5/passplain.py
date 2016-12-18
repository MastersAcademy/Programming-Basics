from plain import Plain  # import Plain class


class PassPlain(Plain):  # class PassPlain is Plain class inheritance

    def __str__(self):
        return 'Ok! this is passenger plane number %s and it is %s' % (self.number, self.color)
