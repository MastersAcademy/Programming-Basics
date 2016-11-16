name = input("What is your name? ")
age = int(input("How old are you? "))
city = input("Where do you live? ")

print("So your name is %s, your are %i,"
      "and you live in %s." % (name, age, city))

file = open("out", "w")
file.write("So your name is %s, your are %i,"
      "and you live in %s." % (name, age, city))