## Homework-2

print ("-=Jiub is the first person you see in the game=-")
print ("Jiub say:")
print ("\"Wake up, we're here. Why are you shaking?")
print ("Are you ok? Wake up.\"")

Name = input("What is your name:")

print ("Jiub say:")
print ("\"Well, not even last night's storm could wake you.")
print ("I heard them say we've reached Morrowind, I'm sure they'll let us go.\"")

phone_book = {"Race": "Race", "Class": "Class", "Sign": "Sign"}

phone_book["Race"] = input("Which race you are:")
phone_book["Class"] = input("What is your class:")
phone_book["Sign"] = input("Upon what sign you were born:")
Level = int(input("Which level your are?:"))

answer = ("Greeting %s %s, you was born under %s sign.\nNow you are rich %i level"
          %(phone_book["Race"], phone_book["Class"], phone_book["Sign"], Level))


print(answer)
print(phone_book)

scroll = open('Ancient_scroll.txt', 'w')
scroll.write(answer)
scroll.write('{}'.format(phone_book))
scroll.close()

