print("Hello. Fill next fields:")
name = input("What is your name? ")
age = int(input("Your age? "))
opinion = input("Do you like 'Python' language? ")
out = "Your answer was: " \
         " 1)What is you name: {};" \
         " 2)Your age? {};" \
         " 3)Do you like 'Python' language? {}".format(name, age, opinion)
print(out + "\nI write all information in file 'log.txt' \nBye!")
stdout = open('log.txt', 'w')
stdout.write(out)
stdout.close()