print("homework-1")
name = input("what is your name?")
age = int(input("How old are you?"))
city = input("Where do you live?")
car = input("You have a car?")

print("Ah, so your name is %s, your age is %s, and you live in %s. Do you have a car %s."" Good!" % (name, age, city,car))

file = open('results.txt', 'w')
file.write(name + "\n")
file.write(str(age) + "\n")
file.write(city + "\n")
file.write(car + "\n")
file.close()
print("Done!")


print("homework-2")
dict_a = {
    "first_name": "Evgen",
    "last_name": "Mushkin",
    "dob": "1989-09-05",
}

print(dict_a)

for k, v in dict_a.items():
    print(k + ": " + v)

dict_a['hobbis'] = ['fishing', 'studing']

dict_b = {
    'cat': {
        'name': 'Murzik',
        'color': 'whit',
        'age': '12'
    }
}
dict_a['pet'] = dict_b
print(dict_a)

print("=== *** manipulation set *** ===")
list_a = [1,2,3,4,4,4,'a',7,8,9,9,9,9,"hi"]
for i in list_a:
    print('|- ' + str(i))


range_1 = range(0, 9)
for i in range_1:
    print('|- ' + str(i))

print(list_a)
print(set(list_a))


print("-=homework-4=-")
print("how much time we spend on training")


int_1 = 4
if int_1 > 1:
    print("|-Positive")
elif int_1 == 2:
    print("|-Slightly")
else:
    print("|-Negative")


int_1 = 2
if int_1 > 2:
    print("|-Positive")
elif int_1 == 2:
    print("|-Slightly")
else:
    print("|-Negative")


print('-= Age =-')
age = 27
if age in range(0, 13):
        print('|- Child')
elif age in range(13, 21):
        print('|- Teenager')
elif age in range(21, 31):
        print('|- Young')
elif age in range(31, 61):
        print('|- Adult')
elif age > 60:
        print('|- Old')
else:
        print('|- Are you sure?')

