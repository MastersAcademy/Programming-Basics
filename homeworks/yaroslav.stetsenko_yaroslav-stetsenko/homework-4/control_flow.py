__author__ = 'Ярослав'


name = str(input (" What is your name? "))
surename = str(input(" Your Surename? "))
age = int(input (" How old are you? "))
country = str(input (" What is your nationality? "))
print("Hello %s %s, you were born %i  years ago, you citizen of %s. Good" % (name, surename, age, country))


print("----Control flow----")

name_surname = (name +' '+ surename)
print (name_surname)

if len(name_surname) <= 6:
    print('|- Sorry, your full name is short')
elif len(name_surname) > 6:
    print('|- Good')
else:
    print('|- Error')



sex = str(input(" Your is Man or woman?"))
print('-Age-')
if age in range(0, 18):
    print(("|- Little %s")%(sex))
elif age in range(21, 31):
    print(("|- Young %s")%(sex))
elif age in range(31, 61):
    print(("|- Middle age %s")%(sex))
else:
    print('|- Are you sure?')



list_1 = (age, age -2, age +6, age +1, age -12)
for i in list_1:
    print('|- ' + str(i))

print('-= PASS =-')
for i in list_1:
    if i < 3:
        pass
    print('|- %i' % i)


