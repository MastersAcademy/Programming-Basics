name = input("what is your name?")
age = int(input("How old are you?"))
city = input("Where do you live?")
car = input("You have a car?")

print("Ah, so your name is %s, your age is %s, and you live in %s. Do you have a car %s."" Good!" % (name, age, city,car))

file = open('results.txt', 'w')
file.write(name + "\n")
file.write(str(age) + "\n")
file.write(city + "\n")
file.write(car + "\n")
file.close()
print("Done!")
