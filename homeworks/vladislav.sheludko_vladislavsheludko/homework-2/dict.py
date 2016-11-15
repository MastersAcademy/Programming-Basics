print ('--- === *** Dictionaries *** === --- ')

name = input('What is your name?')
surname = input('What is your surname?')
age = int(input('How old are you?'))
phone = input('What is your phone?')
city = input('Where do you live?')

dict_inform = {
    'name': name,
    'surname': surname,
    'age': age,
    'phone': phone,
    'city' : city
}

print (dict_inform)

result = (' My name is %s\n Age is %s\n Phone is %s\n I live in %s.\n' ' Wonderful!' % (dict_inform['name'] + ' ' + dict_inform['surname'], dict_inform['age'], dict_inform['phone'], dict_inform['city']))
print(result)

file = open('personal_data.txt', 'w')
file.write(result)
file.close()

