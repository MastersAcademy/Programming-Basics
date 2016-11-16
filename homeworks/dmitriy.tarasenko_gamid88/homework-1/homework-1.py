file = open('input.txt', 'w')

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
