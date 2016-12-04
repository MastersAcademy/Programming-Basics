print('Please answer for a several questions')

name = input('your name: ')
surname = input('your surname: ')
age = int(input('your age: '))
login = input('your login: ')

print('Thanks, your data are saved. You wrote:')
print(' name: %s\n surname: %s\n age: %i\n login: %s' % (name, surname, age, login))

f = open('data.txt', 'w')
f.write("name: " + name + '\n')
f.write("surname: " + surname + '\n')
f.write("age: " + str(age) + '\n')
f.write("login: " + login + '\n')
f.close()

if age in range(1,17):
    f = open('data.txt', 'a')
    f.write("underage" + '\n')
    f.close()
elif age in range(18,100):
    f = open('data.txt', 'a')
    f.write("adult" + '\n')
    f.close()
else:
    f = open('data.txt', 'a')
    f.write("Wrong data" + '\n')
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
f.write("===============================" + '\n')
f.write("Dictionary" + '\n')
f.write(str(d))
f.close()

s = set()
s.add(name)
s.add(surname)
s.add(age)
s.add(login)

print(' ')
print('Preview of Set with User data')
print(' ')
print(s)

f = open('data.txt', 'a')
f.write('\n' + "===============================" + '\n')
f.write("Set" + '\n')
f.write(str(s))
f.close()
