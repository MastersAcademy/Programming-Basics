print('Please answer for a several questions')

name = input('your name: ')
surname = input('your surname: ')
age = int(input('your age: '))
login = input('your login: ')

print('Thanks, your data are saved. You wrote:')
print(' name: %s\n surname: %s\n age: %i\n login: %s' %(name, surname, age, login))

f = open('data.txt', 'w')
f.write("name: " + name +'\n')
f.write("surname: " + surname +'\n')
f.write("age: " + str(age) +'\n')
f.write("login: " + login +'\n')
f.close()

print('===================================================')

d = {}
d["name"] = name
d["surname"] = surname
d["age"] = age
d["login"] = login
print("Preview of Dictionary with user data")
print(' ')
print(d)

f = open('data.txt', 'a')
f.write("===============================" + '\n' )
f.write("Dictionary" + '\n')
f.write(str(d))
f.close()