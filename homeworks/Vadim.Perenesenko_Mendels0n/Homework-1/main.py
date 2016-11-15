name = input("What is your name? ")
age = int(input("What you age? "))
last_name = input("What is your last name? ")

text = "Your name is %s %s, your age is %i. Nice" %(name, last_name, age)
print(text)

file = open("text.txt", "w")
file.write(text)
file.close()

file = open("text.txt", "r")
print("*** Reading file ***")
print(file.read())
