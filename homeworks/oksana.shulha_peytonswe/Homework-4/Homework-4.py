#questionnaire
name = input('What is your name? ')
surname = input('What is your surname? ')
gender = input('What is your gender? m/f ')

while gender != 'm' and gender != 'f': 
    print("Type 'm' or 'f'") 
    gender = input('m/f? ') 
if gender == 'm': 
    gender = 'male' 
elif gender == 'f': 
    gender = 'female' 
    
year_of_birth = int(input("In what year were you born? "))

chinese_calendar = ['rat', 'bull', 'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'sheep', 'monkey', 'cock', 'dog', 'pig']
BASE_YEAR = 1948
position = (year_of_birth - BASE_YEAR) % len(chinese_calendar)

age = int(2016 - year_of_birth)
place_of_birth = input('Where you from? ')
nationality = input('What is your nationality? ')
address = str(input('What is your home address? '))
profession = input('What is your profession? ')
phone_number = str(input('What is your phone number? '))
email_address = str(input('What is your email address? '))

#information
info = str("Well, your name is %s, you're a %s.\n"
       "You was born in %i and you're %i years old.\n"
       "You're from %s, your nationality is %s.\n"
       "You live at %s and your employment is %s.\n"
       "Your contact information: phone %s, email %s.\n"
           % (name + ' ' + surname, gender, year_of_birth,
              age, place_of_birth, nationality,
              address, profession, phone_number, email_address))

print (info)
print ('Your year of birth is {}'.format(chinese_calendar[position]))
if (not year_of_birth % 4 and year_of_birth % 100) or not year_of_birth % 400:
    print('leap year')
else:
    print('non-leap year')


import collections

print ('Dictionary:')

print ('\nOrderedDict:')
d = collections.OrderedDict()

d['name:'] = 'Oksana'
d['surname:'] = 'Shulha'
d['gender:'] = 'Female'
d['year_of_birth:'] = '1994'
d['age:'] = '22'
d['place_of_birth:'] = 'Ukraine'
d['dnationality:'] = 'ukrainian'
d['address:'] = 'Tschaikovsky, 46'
d['profession:'] = 'student'
d['phone_number:'] = '+3(8063)5715155'
d['email_address:'] = 'peytonswe@gmail.com'

for k, v in d.items():
    print (k, v)

print (d)






