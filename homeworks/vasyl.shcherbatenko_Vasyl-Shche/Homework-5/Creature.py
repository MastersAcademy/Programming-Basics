class Creature:

    __name = "n/a"
    __thing_property = "true"
    __ability_to_die = "true"

    def __init__(self, name, thing_property, ability_to_die):
        self.__name = name
        self.__thing_property = thing_property
        self.__ability_to_die = ability_to_die

    def set_name(self, n):
        self.__name = n

    def name(self):
        return self.__name

    def set_thing_property(self, t):
        self.__thing_property = t

    def thing_property(self):
        return self.__thing_property

    def set_ability_to_die(self, n):
        self.__ability_to_die = n

    def ability_to_die(self):
        return self.__ability_to_die

    def description(self):
        print("+++=============================+++")
        print("Hi let a user run the program ")
        print("Name creation ", self.__name)
        print("Can creatures die ", self.__ability_to_die)
        print("Can thinking creatures ", self.__thing_property)
