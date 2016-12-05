import months as months

file = open('results.txt', 'w')

print('Hello, friend!')

list_a = ['Python', 'JavaScript', 'Quality Assurance', 'Ruby on rails']
print (list_a)
print('On what course you want to study?')
print (list_a[0])
print ('***===***')
print('My family')
dict_f = {
    'Wife': {
        'Name': 'Elena',
        'Age': '25'
    },
    'Daughter': {
        'Name': 'Masha',
        'Age': '4'
    }
}
print(dict_f)
print ('****====****')
print('My own hobbies')
list_b = ['Sport', 'Football', 'Traveling', 'Selfdevelopment']
list_b.sort()
print(list_b)

print('What day of the week you would like to attend courses?')
list_1 = ['Monday','Tuesday','Wednesday','Thursday','Friday']
for s in list_1:
    print('° ' + str(s))


print('Please rate your level of English')
eng_rate = int(input('From 0 to 15  -  '))
if eng_rate in range(0, 4):
    print('Beginner, Elementary')
elif eng_rate in range(4, 7):
    print('Pre-Intermediate')
elif eng_rate in range(7, 10):
    print('Intermediate')
elif eng_rate in range(10, 13):
    print('Upper-Intermediate')
elif eng_rate in range(13, 16):
    print('Advanced')
else:
    print('Sorry. Try again!')



name = input('What is your name? ')
surname = input('What is your surname? ')
years = int(input('How old are you? '))
city = input('Where are you from? ')


questions = ('Well, so, your name is %s, your surname %s, you are %i years old, '
             'and you live in %s. \nWelcome to the MastersAcademy, nice to meet you! \nGood luck, student!'
             % (name, surname, years, city))

print(questions)
print()

file.write(questions)
file.close()