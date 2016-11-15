#!/usr/bin/env python3

first_name = input('Your First Name: ')
last_name = input('Your Last Name: ')
age = input('How old are you?: ')

text = 'Hello, %s %s!\nYour age is %s!' % (first_name, last_name, age)

print(text)

file = open('homework_1.txt', 'w')
file.write(text)
file.close()
