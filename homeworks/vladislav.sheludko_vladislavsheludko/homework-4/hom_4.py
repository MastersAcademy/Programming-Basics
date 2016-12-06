
age = int(input('How old are you?'))
phone = input('What is your phone?')
city = input('Where do you live?')

age = int(age)

if age < 18:
    print('You are teenager')
elif age > 18 and age < 30:
    print ('You are young')
else:
    print('Nice')

fullName = input('What is your name and surname?')
while(fullName != 'Vlad Sheludko'):
    print('Error name!')
    fullName = input('What is your name and surname?')

if fullName == 'Vlad Sheludko':
    print('Good!')
else:
    print('Not good!')


dict_inform = {
    'Full name' : fullName,
    'age': age,
    'phone': phone,
    'city' : city
}

print (dict_inform)

result = (' My name is %s\n Age is %s\n Phone is %s\n I live in %s.\n' ' Wonderful!' % (dict_inform['Full name'], dict_inform['age'], dict_inform['phone'], dict_inform['city']))
print(result)


#file = open('personal_data.txt', 'w')
#file.write(result)
#file.close()

