# Homework-2
# second_python_program
# taras.bulba

model_1 = {
    'brand': 'audi',
    'release year': '2015',
    'color': 'white'
}

model_2 = {
    'brand': 'bmw',
    'released year': '2015',
    'color': 'black'
}

question_1 = input('What is your name? ')

print('Hello %s!' % (question_1))

question_2 = input('Do you want to buy a car? ')

if question_2 == 'Yes':
    print('We have some for you! ', model_1['brand'], model_2['brand'])
else:
    print('Sorry!')

question_3 = input('Do you need more information? ')

if question_3 == 'Yes':
    print('There you are!', model_1, model_2)
else:
    print('Sorry!')

question_4 = input('Which model do you choose? ')

print(question_4)

# Writing answer in data file
myfile = open("info.txt", "w")
myfile.write(question_4)
myfile.close()










