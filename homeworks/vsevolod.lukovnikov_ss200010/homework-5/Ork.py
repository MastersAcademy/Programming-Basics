class Ork():
    def __init__(self, name, warclass, weapon):
        self.name = name
        self.warclass = warclass
        self.weapon = weapon

    def fight_the_enemy(self):
        print("I'm fight enemy with my " + self.weapon)

    def about_ork(self):
        return "This is furious and strong ork. He's name - %s,  his warclass is - %s and his favorite weapon of death is - %s" %(self.name, self.warclass, self.weapon)