print("______________________Welcome________________________")
print("If you want to find a job, please fill in the form!!!")

file_info = open("hey.txt", "w")

name = input("What is your name? ")
surname = input("What is your surname ")
age = int(input("How old are you? "))
if age < 18:
    print('Sorry but we do not have work for you =(')


city = input("Where do you live? ")
previous_job = input("Where did you work? ")
experience = input("What is your work experience? ")
if experience > 5:
    check = ('You have the chance')
else:
    check = ('You do not have enough experience')


name_surname = name + ' ' + surname
salary = int(input('How much you want to earn?'))
if salary in range(0, 2000):
    print('It is easy to find')
elif salary in range(2000, 5000):
    print('We will try to find but do not promise')
elif salary in range(5000, 20000):
    print(check)



list_bye = ['Goodbye', name, surname]

info = "Thank you %s, your age is %i. \n We will try to find work in the city %s." \
       " \n Job vacancy - %s \n Experience - %s" % (name_surname, age, city, previous_job, experience)

print(info)
print("We will send you letter, check your postbox.")
print (list_bye)
print("Good luck")

file_info.write(info)
file_info.close()