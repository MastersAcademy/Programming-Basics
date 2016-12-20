from Improved_chair import Improved_chair

class Armchair (Improved_chair):
    def __init__(self, leg_num, material, cover="leather"):
        Improved_chair.__init__(self, leg_num, material)
        self.armrest = "true"
        self.backrest = "true"
        self.cover = cover if cover else leather

    def sit(self):
        return "Its a comfortable %s armchair, have armrest ? %s, have backrest ? %s" % (self.cover,self.armrest, self.backrest)