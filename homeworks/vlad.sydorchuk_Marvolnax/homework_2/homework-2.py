inf = {}

inf['n'] = input('Enter your name: ')
inf['s'] = input('Enter your surname: ')
inf['a'] = int(input('Enter your age: '))
inf['e'] = input('Enter your e-mail: ')
inf['l'] = input('Enter your login: ')

content = open('data.txt', 'w')
list = 'Your data:\nname %s;\nsurname %s;\nage %s;\ne-mail %s;\nlogin %s.' %(inf['n'], inf['s'], inf['a'], inf['e'], inf['l'])
content.write(list)
content.close()

content = open('data.txt', 'r')
print('---Print new file---\n' + content.read())
content.close()
