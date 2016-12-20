dict_name = {
    'Dmitro': {
        'first_stat': 'Admin',
        'skill': 'yes',
        'rum': 'A12',
		'stat_rum': 'yes',
        'password': '123'
    },
    'user_Tin': {
        'first_stat': 'User',
        'skill': 'Not',
        'rum': 'A14',
		'stat_rum': 'Not',
        'password': '125'
    }
 }
print('Hello')
str_name = input("What is your name? ")
if str_name == 'Dmytro' :
    print('Hi Dmytro')
    cont_pass_int = 0
    while cont_pass_int <= 2:
        str_pass = input("Please enter your Password")
        if str_pass == dict_name['Dmitro']['password'] :
            print ('Good Day Dmytro Admin')
            break
        else: print('Are you Dmytro')
        cont_pass_int += 1
elif str_name == 'user_Tin':
    print('Hi User_Tin')
    cont_pass1_int = 0
    while cont_pass1_int <= 2:
        str_pass = input("Please enter your Password")
        if str_pass == dict_name['user_Tin']['password'] :
            print ('Good Day User_Tin')
            break
        else: print('Are you User_Tin')
        cont_pass1_int += 1
else: print('User not create, please contact your administrator')

print('Disconnect')

