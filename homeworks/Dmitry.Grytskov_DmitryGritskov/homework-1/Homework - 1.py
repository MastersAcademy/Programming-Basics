#! usr/bin/env Python3

print ('Hello !')  # collect users data
name = str(input('what is your name ?'))
age = str(input('Ok! how old are you ?'))
country = str(input('Where are you from ?'))

data = 'Name: '+name+ '\n' +'Age:'+age+ '\n' +'City: '+country+ '\n'

print('Ok! your data is:')  # printing users data
print(data)

a_file = open('data.txt','w') # open file and save data in txt-file
a_file.write(data)
a_file.close()

print ('Your data saved in file "data.txt".')