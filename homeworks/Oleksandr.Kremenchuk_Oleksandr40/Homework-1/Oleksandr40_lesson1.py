# This is questionnaire created by Oleksandr
# Defining variables
print('Hello friend! \nIntroduce yourself!')
surname = input('What is your family name? ')
name = input("What is your name? ")
surname_name = name + ' ' + surname
age= int(input("How old are you? "))
country = input('What country do you live in? ')
team = input('What is your favorite football team? ')
answers = [surname, name, age, country, team]
questions =['surname', 'name', 'age', 'country', 'team']

#output variables
print('\n-------------------------')
print(answers, end=',')
print("\nOk! Let's check your data.")
print('\nYou are %s and you are %i yeas old. Great!\n Your motherland is %s,'
       ' and favorite football team is %s.' %(surname_name, age, country, team))

#create&write to a file     
print("\nLet's save your data into a file, and will call it your surname\n")
name_of_file = open(surname, 'w')
s = str(answers)
name_of_file.write(s)
name_of_file.close()

#read from a file and print on the screen
name_of_file=open(surname, 'r')
a=name_of_file.read()
print(a+'\n')
name_of_file.close()
print("Now I'm goint to read from your file.\n-----------------")

for q, a in zip(questions, answers):
     print('What is your {0}?  It is {1}.'.format(q, a))

print('\nTnaks you for your time!!!------')
