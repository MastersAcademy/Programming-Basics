##HomeWork-4 /  Working with input/output and with File methods And Dictionary And FlowControl

print("Hello")
print("Tell about yourself")

# Input var
FirstName = input('Enter your FirstName:')
LastName = input('Enter your LastName:')
Place = input("Whesre are you from:")
Age = int(input("How old are you?"))
Hobby = input("What are you Like:")


# Printing results into command line
Result = ("\n %s %s, you are from %s.\n You are %i years old and you like %s" % (FirstName, LastName, Place, Age, Hobby))
print(Result)


##File methods
#create, open file in write mode
InputText = [FirstName, LastName, Place, Age, Hobby, Result]
with open('base.txt', 'w') as DBFile:
    for line in InputText:
        print(line, file=DBFile)


#Dictionary
Dict = {
    'DFirstName': FirstName,
    'DLastName': LastName,
    'DPlace': Place,
    'DAge': int(Age),
    'DHobby': Hobby,
}

print(Dict)

DictView = ('Dictionary Card : %s' % Dict)
print(DictView)

if Age in range(0,14):
    AgeStatus = 'You Are Children'
elif Age in range(14,23):
    AgeStatus = 'You Are Teenager'
elif Age in range(23,35):
    AgeStatus = 'You Are Young'
elif Age in range(35, 45):
    AgeStatus = 'You Are Adult'
elif Age >= 45:
    AgeStatus = 'You Are Old'
else:
    AgeStatus = 'Are You A Life?'

print(AgeStatus)

DBFile = open('base.txt', 'a')
DBFile.write(DictView)
DBFile.write(AgeStatus)
DBFile.close()
