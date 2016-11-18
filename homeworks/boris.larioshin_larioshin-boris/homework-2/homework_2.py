# Homework 2 using dictionary
print('-----------Please enter your information------------')
# using dictionary
user_data = dict()
user_data['name'] = input("What is your name? ")
user_data['surname'] = input("What is your surname? ")
user_data['age'] = input("How old are you? ")
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
