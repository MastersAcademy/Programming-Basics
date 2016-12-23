name = input("Your name? ")
surname = input("Your surname? ")
age = int(input("Your age? "))
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

message = "Okay, so your full name is %s %s. You are age of %i and you live in %s. " \
       "Today is %s and the weather is %s, and you feel %s" % (user_info['name'], user_info['surname'],
                                                               user_info['age'], user_info['city'],
                                                               user_info['date'], user_info['weather'],
                                                               user_info['mood'])

list_a = [user_info, message]

print(message)
print(list_a)

file = open('info.txt', 'w')
file.write(message)
