from Person import Person
from SunGlasses import SunGlasses

print("We have trouble at hands. Let's find person who can solve it")

person = Person('Bruce Willis', 61, 'Savior')
sunglasses = SunGlasses('RayBan Aviator', 'carbon fibre',
                        'polarized green', 'pilot', 65, 'black')
print(sunglasses)
person.looking_for_glasses(sunglasses)
person.save_the_world()
