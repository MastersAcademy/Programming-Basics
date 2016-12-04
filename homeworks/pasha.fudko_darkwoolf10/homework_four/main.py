import getpass
feedback = False
while feedback != True:
    login = input("Enter login: ")
    #Оно печатает, но как и в терминале не выводит пароль
    password = getpass.getpass()
    if (login == 'admin' or login == "pasha") and password == 'password':
        feedback = True
    else:
        feedbeack = False
print("Hello " + login + "\n" + 30 * '*')
time = int(input("what time is it: "))
if time < 7:
    print("go sleep")
elif time >= 11 and time <= 13:
    print("go breakfast")
elif time >= 6 and time <= 19:
    print("go dinner")
elif time <= 24:
    print("you have written more than 24 hours")
else:
    print("go work")
age = input("How old are you? ")
i = 1
while:
    print("you" + i + "years")
    if i == 19:
        break
    i++
