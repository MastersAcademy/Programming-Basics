# Homework 4 (add control flow)
print('-----------Please enter your information------------')
# using dictionary
user_data = dict()
user_data['name'] = input("What is your name? ")
user_data['surname'] = input("What is your surname? ")
age = input("How old are you? ")
# Add while for check enter age
while age.isdigit() != True:
    print('You have entered incorrect data. Please enter the number (your age)... '+'\n')
    age = input()

user_data['age'] = age

if int(user_data['age']) in range(0, 6):
    user_data['myself'] = 'I am a child. This information is from my parents'
elif int(user_data['age']) in range(6, 16):
    user_data['myself'] = 'I am a schoolkid'
elif int(user_data['age']) in range(16, 21):
    user_data['myself'] = 'I am student'
elif int(user_data['age']) in range(21, 31):
    user_data['myself'] = 'I am yong man(woman)'
elif int(user_data['age']) in range(31, 61):
    user_data['myself'] = 'I am adult man(woman)'
elif int(user_data['age']) in range(61, 101):
    user_data['myself'] = 'I am old man(woman)'
else:
    user_data['myself'] = 'Wow. My real identity Dunkan MacLaud'

user_data['city'] = input("Where do you live? ")
# using list
lang_list = ['english', 'russian', 'ukrainian']
print('Choose your native language. By entering its number:'+'\n')
choice = int(input('1.English'+'\n'+'2.Russian'+'\n'+'3.Ukrainian'+'\n'+'Enter number:'+'\n'))
if choice == 1:
    user_data['lang'] = lang_list[0]
elif choice == 2:
    user_data['lang'] = lang_list[1]
elif choice == 3:
    user_data['lang'] = lang_list[2]
else:
    user_data['lang'] = 'My language is not in the list'
# Print dictionary on screen
for k, v in user_data.items():
    print(k + ': ' + v)
file_out = open('User_profile.txt', 'w')
# Write in file
file_out.write("**********User profile*************\n")
file_out.write(user_data['myself']+'\n')
file_out.write("My name is: "+user_data['name']+'\n')
file_out.write("My surname is: "+user_data['surname']+'\n')
file_out.write("I am "+user_data['age']+" year old"+'\n')
file_out.write("I live in: "+user_data['city']+'\n')
file_out.write("My native language is "+user_data['lang']+'\n')
file_out.write("*************************************")
file_out.close()
# Print on screen
file_in = open('User_profile.txt', 'r')
for line in file_in:
    print(line, end='')