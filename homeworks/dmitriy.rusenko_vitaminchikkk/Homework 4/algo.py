inf = {}

inf['n'] = input('Enter your name: ')
inf['s'] = input('Enter your surname: ')
inf['a'] = int(input('Enter your age: '))
inf['e'] = input('Enter your e-mail: ')
inf['l'] = input('Enter your login: ')

x = 0
while x == 0:
    q = input('Are you sure? (yes/no)')
    if q == 'yes':
        content = 'Your data:\nname %s;\nsurname %s;\nage %s;\ne-mail %s;\nlogin %s.' % (inf['n'], inf['s'], inf['a'], inf['e'], inf['l'])
        print('---Print data---\n' + content)
        x = 1
    elif q == 'no':
        inf['n'] = input('Enter your name: ')
        inf['s'] = input('Enter your surname: ')
        inf['a'] = int(input('Enter your age: '))
        inf['e'] = input('Enter your e-mail: ')
        inf['l'] = input('Enter your login: ')
    else:
        print('Your command is not correct')