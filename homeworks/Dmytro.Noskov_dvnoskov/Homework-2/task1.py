name = input("What is your name? ")
age = int(input("How old are you? "))
city = input("Where do you live? ")

list_input =[]
list_input.append(name)
list_input.append(age)
list_input.append(city)

dict_name = {
    'Dmitry': {
        'first_stat': 'Admin',
        'skill': 'yes',
        'rum': 'A12',
		'stat_rum': 'yes'
    },
    'user': {
        'first_stat': 'User',
        'skill': 'Not',
        'rum': 'A14',
		'stat_rum': 'Not'
    }
 }


if list_input[0] == 'Dmitry' :
    list_input.append(dict_name['Dmitry'])
    result = list_input
    print(result)

else :
    if list_input[0] != 'Dmitry' :
        list_input.append(dict_name['user'])
        result = list_input
        print(result)

file = open('task1.txt', 'w')
file.write(str(result))
file.close()