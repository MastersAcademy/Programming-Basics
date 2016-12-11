# homework-4
#taras.bulba_tabu07


print('~~~Hello~~~')

# if, elif, else

# ex 1
int_1 = 1000
if int_1 < 100:
    print('Yes')
elif int_1 == 100:
    print('Good')
else:
    print('No')

# ex 2
color = input('Set color here ' + str())
if color == 'white':
    print('Yes')
elif color == 'orange':
    print('we have not it')
else:
    print('No')

#ex3
print('---and---')
a, b, c = 1, 3, 5
if a > b and b > c:
    print('False')
else:
    print('True')


print('---or---')
a, b, c = 1, 3, 5
if a > b or b > c:
    print('False')
else:
    print('True')

# while, for in, break, range
print('---while---')
a = 0
while a < 10:
    print(a)
    a += 1


# break
a = 0
while a < 10:
    print(a)
    a += 1
    if a == 5:
        break

# continue
a = 1
while a < 20:
    print(a)
    a += 1
    if a > 10:
        continue
    print('---continue---')

# for in
print('---for in---')
myList = [1, 2, 3, 4, 5,]

for x in myList:
    print(x)

# range
print('---range---')
for x in range(1,100, 10):
    print(x)

# end