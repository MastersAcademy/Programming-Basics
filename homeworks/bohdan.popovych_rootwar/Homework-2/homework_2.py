#!/usr/bin/env python3
user_details = {}

user_details['first_name'] = input('Your First Name: ')
user_details['last_name'] = input('Your Last Name: ')
user_details['age'] = input('How old are you?: ')

text = 'Hello, %s %s!\nYour age is %s!' % (user_details['first_name'], user_details['last_name'], user_details['age'])

print(text)

file = open('homework_2.txt', 'w')
file.write(text)
file.close()
