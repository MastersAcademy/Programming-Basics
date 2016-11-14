# Homework №1
name = input("What is your name? ")
surname = input("What is your surname? ")
age = input("How old are you? ")
city = input("Where do you live? ")
file_out = open('User_profile.txt', 'w')
# Write in file
file_out.write("**********User profile*************\n")
file_out.write("My name is: "+name+'\n')
file_out.write("My surname is: "+surname+'\n')
file_out.write("I am "+age+" year old"+'\n')
file_out.write("I live in: "+city+'\n')
file_out.write("*************************************")
file_out.close()
# Print on screen
file_in = open('User_profile.txt', 'r')
for line in file_in:
    print(line, end='')

