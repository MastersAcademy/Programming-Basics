n = input('Enter your name:')
s = input('Enter your surname:')
a = int(input('Enter your age:'))
e = input('Enter your e-mail:')
l = input('Enter your login:')

content = open('data.txt', 'w')
list = 'Your data:\nname %s;\nsurname %s;\nage %s;\ne-mail %s;\nlogin %s.' %(n, s, a, e, l)
content.write(list)
content.close()

content = open('data.txt', 'r')
print('---Print new file---\n' + content.read())
content.close()