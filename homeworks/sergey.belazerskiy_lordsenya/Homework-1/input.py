
name = input("What is your name? ")
age = int(input("How old are you? "))
city = input("Where  you from? ")
work = input("Where you work?")

print("Aha, so your name, and you work at %s is %s, and your age is %i, "
"and you live in %s. great!" % (name, work, age, city))
my_File = open("homework1",'w+',1)
my_File.write("Dear" + name + "\n")
my_File.write("You work at" + work + "in" + city + "\n")
my_File.write("Your age" +str(age))
my_File.close()
