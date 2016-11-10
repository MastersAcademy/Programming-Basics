name = input('your name: ')
surname = input('your surname: ')
login = input('your login: ')

print('Thanks, your data is saving. You write:')
print(name, surname, login)

f = open('data.txt', 'w')
f.write(name +'\n')
f.write(surname +'\n')
f.write(login +'\n')
f.close()