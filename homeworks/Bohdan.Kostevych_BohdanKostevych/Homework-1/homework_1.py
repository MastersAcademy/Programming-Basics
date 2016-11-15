name = input("What is your name?")
city = input("Where do you live?")
age = input("How old are you?")
street = input("Write your street")

all_answers = (
    'Your name is: %s \n You live in: %s \n You are: %s \n Your street is named: %s' % (name, city, age, street))

doFile = open('Answers.txt', "w")
doFile.write(all_answers)
doFile.close()
