print('Hi, please input information about you')

name = input('What is your name?\n')
surname = input('What is your surname?\n')
age = int(input('How old are you?\n'))
city = input('Where are you live?\n')
email = input('What is your e-mail?\n')
phone = int(input('What is your phone?\n'))

result = ("Your name is %s %s, you are %i years old,you live in %s,and your contact information is:\n e-mail: %s \n phone: %i" % (name,surname,age,city,email,phone))
file = open('bio.txt','w')
file.write(result)
file.close()
print (result,'\n','All information saved,thank you')
