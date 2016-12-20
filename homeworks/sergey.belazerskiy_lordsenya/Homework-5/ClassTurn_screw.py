class ClassTurn_screw(object):
    def __init__(self,haft,workingPart):
        self.haft = haft
        self.workingPart = workingPart

    def __str__(self):
        return "haft: %\n workingPart: %s\n" % (self.haft, self.workingPart)

    def working(self):
        return "%s" %("krut")