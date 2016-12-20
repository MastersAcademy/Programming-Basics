# Conditional operator

print('Before you go to a page with the data you need to answer some questions')

userLogin = str(input('Enter your login '))

if userLogin == 'John Smith':

    userPassword = input('Enter your password ')

    if userPassword == 'pass':
        print('Welcome', userLogin, '!')
        print('Your bank account 0 hryvnia')

    elif userPassword == None:
        print('entry canceled')

    else:
        print('incorrect password')

elif userLogin == None:
    print('entry canceled')

else:
    print('I do not know you')

# - and - or

print('two correct options')
age_user = int(input('Enter your age '))
passport_user = str(input('Do you have a passport? '))

if age_user >= 16 and passport_user == 'yes':
    print('True')
else:
    print('False')

print('one correct value')
numberValue = age_user

if numberValue <= 30 or numberValue >= 18:
    print('You are ideal)')

elif numberValue <= 75 or numberValue >= 60:
    print('Time to think about retirement')

else:
    print('Think about it')

# Cycles

print('In order to cooperate with us, please fill in the form!')

user_login = userLogin
userAge = age_user
numberMobile = int(input('Enter your number '))

allInformation = [user_login, userAge, numberMobile]
index = 0

for userInfo in allInformation:
    print(index, ' ', allInformation[index], sep='')
    index += 1
