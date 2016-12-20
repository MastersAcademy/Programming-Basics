#Create dictionaries
dict_q = {
    'name' : str(input("Enter your name: ")),
    'surname':str(input("Enter youre surname: ")),
    'age':int(input("How old are you? ")),
    'city':str(input("Where do you live? ")),
    'game':str(input("Enter your favorite game: "))
}

#output on display dictionaries
print (dict_q)
print ('------------------------*********------------------------')

#date of birth
import datetime
print('Enter your date of birth')
year = int(input("Year->  "))
month = int(input("Month->  "))
day = int(input("Day->  "))
dob = datetime.date(year,month,day)
print (dob)
print ('------------------------*********------------------------')
#--IF--,--Range--
print ('Your horoscope year is: ')
range_1 = range(1912,3000,12)
range_2 = range(1913,3000,12)
range_3 = range(1914,3000,12)
range_4 = range(1915,3000,12)
range_5 = range(1916,3000,12)
range_6 = range(1917,3000,12)
range_7 = range(1918,3000,12)
range_8 = range(1919,3000,12)
range_9 = range(1920,3000,12)
range_10 = range(1921,3000,12)
range_11 = range(1922,3000,12)
range_12 = range(1923,3000,12)
if year in range_1:
    print('|- Крыса')
elif year in range_2:
    print('|- Бык')
elif year in range_3:
   print('|- Тигр')
elif year in range_4:
   print('|- Кролик')
elif year in range_5:
    print('|- Дракон')
elif year in range_6:
    print('|- Змея')
elif year in range_7:
    print('|- Лошадь')
elif year in range_8:
    print('|- Коза')
elif year in range_9:
    print('|- Обезьяна')
elif year in range_10:
    print('|- Петух')
elif year in range_11:
   print('|- Собака')
elif year in range_12:
    print('|- Свинья')
else:
    print('|- Нет данных')
    
#output on display
print ('------------------------*********------------------------')
n = "Name: %s \n"%(dict_q['name'])
s = "Surname: %s \n"%(dict_q['surname'])
a = "Age: %i \n" %(dict_q['age'])
c = "City: %s \n" %(dict_q['city'])
g = "Game: %s \n" %(dict_q['game'])
print(n)
print(s)
print(a)
print(c)
print(g)
print ('--------Thank you!--------')

#Pause in console
import time
time.sleep(20)




