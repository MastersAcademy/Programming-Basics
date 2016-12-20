print('-------------------------------')
name = input("Enter your name:")
surname = input("Enter your surname:")
usr_inf = {
            "name": name,
            "surname": surname,
            }
for t, v in usr_inf.items():
    print(t + ": " + v)

print(usr_inf)


count = int(input('What type of deposit you choose? set the number of days'))
if count in range(0, 90):
    print(usr_inf['name'], ', We open deposit on 12%', 'and', count, 'days')
elif count in range(90, 180):
    print(usr_inf['name'], ', We open deposit on 14%', 'and', count, 'days')
elif count in range(180, 360):
    print(usr_inf['name'], ', We open deposit on 16%', 'and', count, 'days')
else:
    print(usr_inf['name'], ', Unfortunately we can not accept your request')







