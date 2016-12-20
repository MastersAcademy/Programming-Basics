# Ask user some questions and write answers to file


# Define variables
answers = {}
full_name = ''
salary = ''
age = ''

# Questions and answers about user
print('Hello, dear customer! We need some info to register you.')
print('')
print('Please, enter your full name which must contain at least 1 character: ')
while len(full_name) < 1:
    full_name = input('What is your full name? ')
answers['Full name'] = full_name


print('')
print('Please, enter your age which we believe is greater than 0: ')
while not age.isdigit():
    age = input('What is your age? ')
if int(age) <= 0:
    age = '1'
    print('So you did not listen! Now your age is 1.')
elif int(age) in range(1, 21):
    print('Your age is ' + age + '. That means no alcohol.')
else:
    print('Wow, you are old enough to drink alcohol. Enjoy!')
answers['Age'] = age


print('')
print('Please, enter your salary which must contain only digits: ')
while not salary.isdigit():
    salary = input('What is your approximate salary(USD)? ')
answers['Salary'] = salary


print('')
answers['Answer'] = input('What is the Answer to the Ultimate Question of Life, the Universe, and Everything? ')


# Printing
print('')
print('')
print('Your name is %s, and you are %s years old, your approximate salary is %s USD, '
      'and the Answer to the Ultimate Question of Life, the Universe, '
      'and Everything is %s.' % (answers['Full name'], answers['Age'], answers['Salary'], answers['Answer']))
print('Thank you! Have a nice day!')

# Operations with file in the current working directory
f = open("answers.txt", "w")
f.write(' === Information about user === \n')

for k, v in answers.items():
    f.write(k + ': ' + v + '\n')

f.write(' === End of file === ')
f.close()
