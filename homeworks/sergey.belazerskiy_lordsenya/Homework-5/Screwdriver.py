from ClassTurn_screw import ClassTurn_screw


class Screwdriver (ClassTurn_screw):
    def __init__(self,haft,workingPart,watt):
        ClassTurn_screw.__init__(self,haft,workingPart)
        self.watt = watt

    def motor(self):
        return "%s" % ("wgg-krut")

