from Ork import Ork

class Ork_Archer(Ork):
    def __init__(self, name, weapon):
        Ork.__init__(self,name,"archer", weapon)

    def need_arrows(self):
        if self.weapon == "bow":
            print("I need arrows")
        else:
            print("I don't need any arrows!")


archer = Ork_Archer("Durotar", "bow")

print(archer.warclass)
archer.need_arrows()
archer.fight_the_enemy()
print(archer.about_ork())

class Ork_Warrior(Ork):
    def __init__(self, name, weapon):
        Ork.__init__(self, name, "warrior", weapon)


    def warcry(self):
        print("I'm %s and I kill'em all" %(self.name))


warrior = Ork_Warrior("Check", "Hammer of Death")

warrior.fight_the_enemy()
warrior.warcry()
# warrior.need_arrows() # must be Error
print(warrior.about_ork())

