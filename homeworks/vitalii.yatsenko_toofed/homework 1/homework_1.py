#Questionnaire by Vitalii Yatsenko

FirstName = str(input('Write your first name - '))
Surname = str(input('Write your surname - '))
Age = (input('How old are you (in years)? - '))

while Age.isdigit()!= True:
	print('Write number please..')
	Age = (input('How old are you (in years)?'))

Age = int(Age)
Gender = str(input('What is your gender? - '))
Address = str(input('Where are you from? - '))
Emloyment = str(input('What is your employment status? - '))

print('---So check what you are write---')

print('Your full name is %s %s' %(FirstName, Surname))
FullName = FirstName + ' ' + Surname
print('Check one more time - %s' %FullName)
FullName = "%s %s" %(FirstName, Surname)
print('Check the last time - %s' %FullName)

print('You are %i years old' %Age)
print('Your gender is %s and you live in %s' %(Gender, Address))

FullInformation = "Your name is %s %s and your gender is %s. Your age is %i. You live in %s and you are %s." %(FirstName, Surname, Gender, Age, Address, Emloyment)   
file = open('Information.txt', 'w')
file.write(FullInformation)
file.close()

print('---Check file content---')
FileCheck = open('Information.txt', 'r')
CheckString = FileCheck.read()
print(CheckString)