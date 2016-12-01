print('--- ===  ***  === ---')
print('-= IF ELSE statement =-')
str_1 = ''
if not str_1:
    print('|- Sting is blank')


int_1 = 125
if int_1 > 0:
    print('|- Positive')
elif int_1 == 0:
    print('|- Zero')
else:
    print('|- Negative')


if int_1:
    print('|- True')


if not int_1:
    print('|- False')


print('')
print('')
print('--- ===  ***  === ---')
print('-= FOR statement =-')
list_1 = [1, 2, 3, 4, 5]
for i in list_1:
    print('|- ' + str(i))


print('')
print('')
print('--- ===  ***  === ---')
print('-= RANGE =-')
range_1 = range(0, 5)
for i in range_1:
    print('|- ' + str(i))


print('-= Age =-')
age = 25
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


print('-= Range steps =-')
print(list(range(0, 50, 2)))
print(list(range(0, 50, 3)))
print(list(range(50, -50, -4)))


print('')
print('')
print('--- ===  ***  === ---')
print('-= WHILE statement =-')
counter_1 = 0
while counter_1 <= 15:
    print('|-' + str(counter_1))
    counter_1 += 1


counter_2 = 0
for i in list_1:
    print('|- index: %i | element: %i' % (counter_2, i))
    counter_2 += 1


print('')
print('')
print('--- ===  ***  === ---')
print('-= BREAK, CONTINUE, PASS statement =-')
counter_3 = 0
print('-= BREAK =-')
for i in list_1:
    if i == 3:
        break
    counter_3 += 1


print('|- index of 3: %i' % counter_3)
print('-= Continue =-')
for i in list_1:
    if i < 3:
        continue
    print('|- %i' % i)


print('-= PASS =-')
for i in list_1:
    if i < 3:
        pass  #TODO Implement feature
    print('|- %i' % i)

