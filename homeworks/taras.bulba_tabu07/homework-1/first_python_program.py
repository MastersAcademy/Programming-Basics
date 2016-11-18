# Homework-1
# first_python_program
# taras.bulba


name = input('What is you name? ')
age = int(input('How old are you? '))
city = input('Where are you from? ')

hello = "Hello %s! I see you are %s and from %s. You are welcome!" % (name, age, city)

print(hello)

# Writing answer in data file
myfile = open("info.txt", "w")
myfile.write(hello)
myfile.close()


