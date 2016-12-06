
#IF Else
number = int(input("    How many books you read for last three month?\n"))
if number in range(0, 2):
      Print ('   Try better')
elif number in range(2, 6):
      print ('   Good work')
elif number in range(6, 100):
      print ('   Exellent')
else:
      print ('   Nice joke')

#For
print ('Prices')
print('')
list_price = [67, 89, 35, 86, 12]
print (list_price)
print('')
print('But prices will grow')
print('new prices is:')
for i in list_price:
    print( '1'+ str(i))

#Range steps
print('')
print('')
print(list(range(17, 38, 3)))
print(list(range(90, -8, -14)))

#WHILE statement
list_p = [12, 13, 14, 15, 16, 17]
print('')
print('')
counter_1 = 13
while counter_1 <= 17:
    print('8' + str(counter_1))
    counter_1 += 1



