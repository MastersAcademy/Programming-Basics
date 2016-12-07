age = int(input("Your age? "))
if age < 18:
    print('Get lost, kid')
elif age > 65:
    print('What are you doing here?')
else:
    name = input("Your name? ")
    surname = input("Your surname? ")
    city = input("City where you live? ")
    date = input("What date is it today? ")
    weather = input("What about weather atm? ")
    mood = input("How do you feel today? ")

user_info = {
    'name': name,
    'surname': surname,
    'age': age,
    'city': city,
    'date': date,
    'weather': weather,
    'mood': mood
}

for answers in user_info:
    print("Your %s is : %s" % (answers, user_info[answers]))
