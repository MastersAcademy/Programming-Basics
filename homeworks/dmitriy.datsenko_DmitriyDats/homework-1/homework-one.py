# the variable is assigned a demo file
fileName = 'demo.txt'
# It opens the file for writing only. Index stands at the beginning of
# the file. Creates a file with the filename, if such does not exist.
accessMode = 'w'
# is input from the console
name = input('What is your name? ')
surname = input('What is your surname? ')
city = input('Where do you live? ')
age = int(input('How old are you? '))
hobby = input('What is your hobby? ')
request_my_data = (' I %s %s \n my hometown %s \n I am %i \n my hobby %s' % (name, surname, city, age, hobby))
# Opening and closing a file
myFile = open(fileName, accessMode)
myFile.write(request_my_data)
myFile.close()