from Creature import Creature
from God import God
from Human import Human

god = God("True", "True", "true")

god.creation()
god.description_of_god()

creature = Creature("Ivan", "True", "true")
creature.description()

people1 = Human("Ivan", "True", " Man", "true")
print("Gender which has ", people1.gender)
