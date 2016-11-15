## Firsthomework

# Jiub is the first person you see in the game

print ("Wake up, we're here. Why are you shaking?")
print ("Are you ok? Wake up.")

Name = input("What is your name:")

print ("Well, not even last night's storm could wake you.")
print ("I heard them say we've reached Morrowind, I'm sure they'll let us go.")

Race = input("Which race you are:")
Class = input("What is your class:")
Sign = input("Upon what sign you were born:")
Level =int(input("Which level your are?"))

answer = ("Greeting %s %s, you was born under %s sign.\n Now you are rich %i level" %(Race, Class, Sign, Level))
print(answer)

scroll = open('Ancient_scroll.txt', 'w')
scroll.write(answer)
scroll.close()

