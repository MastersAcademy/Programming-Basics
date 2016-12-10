print('-------------------------------')
count = 0
count = int(input('What type of deposit you choose? set the number of days'))
bonus = int(input('You can get more %,enter a number from 0 to 4'))

list_1 = [1, 0, 2, 3, 4]
i = 0
for i in list_1:
    if i == bonus:
        break
    i += 1
print('You have bonus', list_1[i], '%')

deposit_count = [12, 14, 16]
if count in range(0, 90):
    bonus_ = deposit_count[0] + list_1[i]
    print('You standard deposit', deposit_count[0], '% on', count, 'days', )
    print('You have bonus', list_1[i], '%')
    print('We open deposit on', bonus_, '%', 'and', count, 'days')
elif count in range(91, 180):
    bonus_ = deposit_count[1] + list_1[i]
    print('You standard deposit', deposit_count[1], '% on', count, 'days', )
    print('You have bonus', list_1[i], '%')
    print('We open deposit on', bonus_, '%', 'and', count, 'days')
elif count in range(181, 360):
    bonus_ = deposit_count[2] + list_1[i]
    print('You standard deposit', deposit_count[2], '% on', count, 'days', )
    print('You have bonus', list_1[i], '%')
    print('We open deposit on', bonus_, '%', 'and', count, 'days')
else:
    print('Unfortunately we can not accept your request')







