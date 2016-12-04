#! usr/bin/env Python3

a_dict = {} # empty dict. will be used to save user data
a_list_of_keys = [] # emty list. will be used to save dict. keys and to show user data in correct way

class DictItem():  # this class will help us to create a_dict with user data in it
    question = str
    key = str
    def adder(self, key, question):
        print(question)
        a_dict[key] = input()
        a_list_of_keys.append(key)

# start to collect user data
f = DictItem()
f.adder('Name:', 'What is your name?')
f.adder('Age:', 'How old are you?')
f.adder('City:', 'Where are you from?')

age = int(a_dict['Age:'])  # trying to collect info about user`s education
if age <=14:
    f.adder('School:', 'Your school number is?')
elif age <=16:
    f.adder('College:', 'Your college name is ?')
else:
    f.adder('University:', 'Your university name is ?')


print('===Bonus Question===')  # stupid joke for user
f.adder('Mind about CA lessons:', 'Do you like Code Academy lessons ?')


var = 0
while var >= 0:
    input('And now ?')
    var += 1
    if var == 3:
        print('Very well ))')
        break


print('===Your data is===')


for i in a_list_of_keys:  # output of user data on screen
    print(i, a_dict[i])