name = input("Your name? ")
surname = input("Your surname? ")
age = int(input("Your age? "))
city = input("City where you live? ")
date = input("What date is it today? ")
weather = input("What about weather atm? ")
mood = input("How do you feel today? ")


info = "Okay, so your full name is %s %s. You are age of %i and you live in %s. " \
       "Today is %s and the weather is %s, and you feel %s" % (name, surname, age, city, date, weather, mood)
print(info)

file = open('info.txt', 'w')
file.write(info)