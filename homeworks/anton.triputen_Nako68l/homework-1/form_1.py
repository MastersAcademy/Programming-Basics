import time
from datetime import date
print("✰✰✰✰✰✰✰✰✪✪✪✪✪✪✯✯✯✯✵✯✯✯✯✪✪✪✪✪✪✰✰✰✰✰✰✰✰")
name = input("Your name is..")
print("Hello", name,"it is the date of your birthday calculator" )
today = date.today()
day_b = int(input("The day of your birthday is.."))
month_b = int(input("The month of your birthday is.."))
your_b = date(today.year, month_b, day_b)
if your_b < today :
 your_b = your_b.replace(year=today.year + 1, )
time_to_b = abs(your_b - today)
conclusion = ("%s it is %s to your birthday"%(name,time_to_b))
print(conclusion)
print("✰✰✰✰✰✰✰✰✪✪✪✪✪✪✯✯✯✯✵✯✯✯✯✪✪✪✪✪✪✰✰✰✰✰✰✰✰")

z = open('file_1.txt', 'w')
z.write(conclusion)
z.close()

