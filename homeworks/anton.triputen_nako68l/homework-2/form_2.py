import time
from datetime import date
name = input("Your name is..")
print("Hello", name,"it is the calculator of days to your birthday" )
today = date.today()
day_b = int(input("The day of your birthday is.."))
month_b = int(input("The month of your birthday is.."))
your_b = date(today.year, month_b, day_b)
if your_b < today :
 your_b = your_b.replace(year=today.year + 1, )
time_to_b = abs(your_b - today)
conclusion = ("%s it is %s to your birthday"%(name,time_to_b))
print(conclusion)
#second hw
list_information = [name, today, day_b, month_b]
print('Information from keyboard - ', list_information)
dict_inf = {
    'Today is': date.today(),
    'tomorow is': today.replace(day = today.day + 1),
    'last month wos': today.replace(month = today.month - 1)
}
print('Date information - ', dict_inf)
dict_inf['Ur_inf'] = list_information
print('Adding list to dictionary - ', dict_inf)
list_information.remove(name)
list_information.append('MastersAcademy')
list_information.extend('javascript')
print('Some changes',list_information)
set_information = set(list_information)
print('sorting list', set_information)

z = open('file_2.txt', 'w')
z.write(conclusion)
z.close()