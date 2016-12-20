class Chair():
    def __init__(self, leg_num=4):
        self.leg_num = int(leg_num)

    def sit(self):
        return "Simple %s Legged chair" % (str(self.leg_num))
