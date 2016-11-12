name = input("What is your name? ")
age = int(input("How old are you? "))
city = input("Where do you live? ")

print (" Your name is =", name)
print (" Your age is =", age)
print (" You live in =", city)

result = 'name - %s, age - %s, city - %s .'%(name, age, city)
file = open('info.txt', 'w')
file.write(result)
file.close()
