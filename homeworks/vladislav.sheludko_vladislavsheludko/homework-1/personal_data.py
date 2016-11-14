print('Hello! Please input your personal data.')
name = input('What is your name?')
surname = input('What is your surname?')
age = int(input('How old are you?'))
email = input('What is your e-mail?')
city = input('Where do you live?')

result = (' My name is %s\n Age is %s\n E-mail is %s\n I live in %s.\n' ' Wonderful!' % (name + ' ' + surname, age, email,city))
file = open('data.txt', 'w')
file.write(result)
file.close()
print('Ok!')

