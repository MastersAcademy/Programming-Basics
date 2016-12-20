from Chair import Chair

class Improved_chair(Chair):
    def __init__(self, leg_num , material):
        Chair.__init__(self, leg_num)
        self.material= material

    def sit(self):
        return "Its %s Legged chair, made from %s" % (str(self.leg_num),self.material)


