from SunGlasses import SunGlasses


class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def looking_for_glasses(self, glasses):
        if glasses.__class__ == SunGlasses:
            print("Found my sunglasses. I'm good to go!")
        else:
            print("I can't do anything without my sunglasses")

    def save_the_world(self):
        if self.name == 'Bruce Willis':
            print('I never wanted this')
        else:
            print('Oh well, we are doomed..')
