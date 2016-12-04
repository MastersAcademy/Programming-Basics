# by Vitalii Yatsenko

firstName = str(input('Write your first name - '))
surname = str(input('Write your surname - '))
age = (input('How old are you (in years)? - '))

while age.isdigit()!= True:
    print('Write number please..')
    age = (input('How old are you (in years)?'))

age = int(age)

if age<18:
    print('You are small yet')
elif age<21:
    print ('You can\'t buy strong alcohol')
else:
    print('Buy what you want')

gender = str(input('What is your gender(M or W)? - '))
while (gender!='M') and (gender!='W'):
    print('Write M or W please..')
    gender = str(input('What is your gender(M or W)? - '))

if gender == 'M':
    gender='Men'
else:
    gender='Women'

address = str(input('Where are you from? - '))
employment = str(input('What is your employment status? - '))

print('---So check what you are write---')

print('Your full name is %s %s' %(firstName, surname))
fullName = firstName + ' ' + surname
print('Check one more time - %s' %fullName)
fullName = "%s %s" %(firstName, surname)
print('Check the last time - %s' %fullName)

print('You are %i years old' %age)
print('Your gender is %s and you live in %s' %(gender, address))

fullInformation = "Your name is %s %s and your gender is %s. Your age is %i. You live in %s and you are %s." %(firstName, surname, gender, age, address, employment)   
print(fullInformation)

print ('\n---===+++|||+++====---\n')

userInformation = []
userInformation.append(firstName)
userInformation.append(surname)
userInformation.append(age)
userInformation.extend(gender)
del userInformation[3]
userInformation.pop()

print (userInformation)
userInformation.clear()
print (userInformation)

testSortList = [10,3,1995,8, 12, 1994, 20,8,1994,4,11,1994]
for i in range(len(testSortList)):
    for j in range(len(testSortList)):
        if testSortList[i] < testSortList[j]:
            temp = testSortList[i]
            testSortList[i] = testSortList[j]
            testSortList[j] = temp
print ('---OwnSort---')
print (testSortList)
print ('---list range---')
print(list(range(0, 51, 5)))
print(list(range(33, -33, -3)))
print ('---break---')

for x in range(1,11):
    if x==7:
        break
    print (x)
else:
    print ('finish without break')

print ('----testing for else----')
for x in range(1,11):
    if x<0:
        print(x)        
        break
else:
    print ('finish without break')

print ('---continue---')
for x in range(1,10):
    if x<7:
        continue
    print (x)
print ('---pass---')
for x in range(1,10):
    if x<7:
        pass
    print (x)

print (sorted(testSortList))
print (testSortList)
testSortList.sort()
print (testSortList)

testSet = set(testSortList)
print (testSet)
testSet = list(testSet)
print (testSet)

userDict = {
    fullName     :    {
            'Age'     :    age,
            'Gender':    gender,
            'Addres':    address,
            'Employment': employment
        }
    }

print (userDict)

if userDict[fullName]['Age'] == age:
    print('age equal')

userDict['Hobbies'] = ['rock-band The Signs (guitar)', 'football']
print (userDict.keys())
print (userDict[fullName]['Employment'])

for k, v in userDict.items():
    print (k + ' - '+ str(v))

del userDict[fullName]['Gender']

for k, v in userDict.items():
    print ('%s === %s' %(k,v))

# file = open('Information.txt', 'a')
# file.write('\n' + str(userDict))
# file.close()

# print('---Check file content---')
# fileCheck = open('Information.txt', 'r')
# checkString = fileCheck.read()
# print(checkString)
