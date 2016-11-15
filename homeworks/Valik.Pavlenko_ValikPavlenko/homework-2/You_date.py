name = input('Your name: ')
surname = input('Your surname: ')
age = int(input('Your age: '))
login = input('Your login: ')
dob = input('Your birthday: ')
print('Thanks, your data are saved. You wrote:')
print(' name: %s\n surname: %s\n age: %i\n login: %s\n dob: %s' %(name, surname, age, login, dob))

f = open('you_data.txt', 'w')
f.write("Name: " + name +'\n')
f.write("Surname: " + surname +'\n')
f.write("Age: " + str(age) +'\n')
f.write("Login: " + login +'\n')
f.write("Dob:" + dob +'\n')
f.close()

print('@@@ $$$ === === $$$ @@@')

b = {}
b["Name"] = name
b["Surname"] = surname
b["Age"] = age
b["Login"] = login
b["Dob"] = dob
print("Preview of Dictionary with user data")
print(' ')
print(b)

f = open('you_data.txt', 'a')
f.write("@@@ $$$ === === $$$ @@@" + '\n' )
f.write("Dictionary" + '\n')
f.write(str(b))
f.close()
