myList = ['Pasha', 'Cherkassy', '19', 'student']

person = {
    'first_name' : 'Pasha',
    'last_name'  : "Fud'ko",
    'dob'        : '1997-03-09',
    'mySity'     : 'Cherkassy'
}
myList.append('programmist')
print(sorted(myList, reverse=True))
print('------------------------------------------')
print(myList)
print('------------------------------------------')
for a, b in person.items():
    print(a + ' : ' + b)
print('------------------------------------------')
myHobbies = ['basketbol', 'coding', 'history', 'physics', 'games']
print(set(myHobbies))
del myHobbies[4]
print(set(myHobbies))
print(myHobbies.count('coding'))
myHobbies.sort()
print(myHobbies)
