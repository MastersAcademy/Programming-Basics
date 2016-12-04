## Homework-4

print ("-=Jiub is the first person you see in the game=-")
print ("Jiub say:")
print ("\"Wake up, we're here. Why are you shaking?")
print ("Are you ok? Wake up.\"")

Name = str(input("What is your name:"))
if Name == "Dragonborn":
    print ("It's Morrowind")
else:
    print ('Greatings %s' %(Name))

print ("Jiub say:")
print ("\"Well, not even last night's storm could wake you.")
print ("I heard them say we've reached Morrowind, I'm sure they'll let us go.\"")

phone_book = {"Race": "Race", "Class": "Class", "Sign": "Sign"}

phone_book["Race"] = str(input("Which race you are:"))
if phone_book["Race"] == "High Elf":
    print ("are you from thalmor embassy high elf?")
else:
    print (phone_book["Race"])
phone_book["Class"] = str(input("What is your class:"))
if phone_book["Class"] == "Rogue":
    print ("Whom i talking to?")
else:
    print (phone_book["Class"])
phone_book["Sign"] = str(input("Upon what sign you were born:"))
if phone_book["Sign"] == "Lady":
    print ("Milady")
else:
    print (phone_book["Sign"])
Level = int(input("Which level your are?:"))
if Level >= 100:
    print ("It\'s not WOW man")
elif Level >= 20:
    print ("You was here before, wasn\'t you?")
else:
    print ("Nice")

answer = ("Greeting %s %s, you was born under %s sign.\nNow you are rich %i level"
          %(phone_book["Race"], phone_book["Class"], phone_book["Sign"], Level))

print(answer)
print(phone_book)

scroll = open('Ancient_scroll.txt', 'w')
scroll.write(answer)
scroll.write('{}'.format(phone_book))
scroll.close()





