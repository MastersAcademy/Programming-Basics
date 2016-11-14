print ("Hello. Answer for a several questions")
name = input("What is your name? ")
surname = input("What is your surname? ")
age = input("Thankyou. How old are you? ")
city = input("Where are you live? ")

results = "Good. Your name is %s %s, your age is %s, you live in %s." %(name, surname, age, city)

print(results)

file = open('data.txt', 'w')
file.write(results)
file.close()
print("Thankyou, your data is saveing. You can see them.")

file = open("data.txt", "r")
