import os, datetime
#import urllib3

days = range(1,32,1)
month = range(1,13,1)
print(month)

cust_birth = dict()
#http = urllib3.PoolManager()

mn = 0
while mn == 0 :
    cust_birth["month"] = int(input ("Provide your birthday month (1-12) => "))
    cust_birth["day"] = int(input ("Provide your birthday day (1-31) => "))
    if (cust_birth["month"] in month) and (cust_birth["day"] in days) :
        mn =1
    else :
        print ("Take another try...")

if ((cust_birth["month"] == 1) and (cust_birth["day"] in range(21,32,1))) or ((cust_birth["month"] == 2) and (cust_birth["day"] in range(20))):
    print ("Your zodiac sign Aquarius")
elif ((cust_birth["month"] == 2) and (cust_birth["day"] in range(20,29,1))) or ((cust_birth["month"] == 3) and (cust_birth["day"] in range(21))):
    print ("Your zodiac sign Pisces")
elif ((cust_birth["month"] == 3) and (cust_birth["day"] in range(21,32,1))) or ((cust_birth["month"] == 4) and (cust_birth["day"] in range(21))):
    print ("Your zodiac sign Aries")
elif ((cust_birth["month"] == 4) and (cust_birth["day"] in range(21,31,1))) or ((cust_birth["month"] == 5) and (cust_birth["day"] in range(21))):
    print ("Your zodiac sign Taurus")
elif ((cust_birth["month"] == 5) and (cust_birth["day"] in range(21,32,1))) or ((cust_birth["month"] == 6) and (cust_birth["day"] in range(22))):
    print ("Your zodiac sign Gemini")
elif ((cust_birth["month"] == 6) and (cust_birth["day"] in range(22,31,1))) or ((cust_birth["month"] == 7) and (cust_birth["day"] in range(23))):
    print ("Your zodiac sign Cancer")
elif ((cust_birth["month"] == 7) and (cust_birth["day"] in range(23,32,1))) or ((cust_birth["month"] == 8) and (cust_birth["day"] in range(24))):
    print ("Your zodiac sign Lion")
elif ((cust_birth["month"] == 8) and (cust_birth["day"] in range(24,32,1))) or ((cust_birth["month"] == 9) and (cust_birth["day"] in range(24))):
    print ("Your zodiac sign Virgo")
elif ((cust_birth["month"] == 9) and (cust_birth["day"] in range(24,31,1))) or ((cust_birth["month"] == 10) and (cust_birth["day"] in range(24))):
    print ("Your zodiac sign Libra")
elif ((cust_birth["month"] == 10) and (cust_birth["day"] in range(24,32,1))) or ((cust_birth["month"] == 11) and (cust_birth["day"] in range(23))):
    print ("Your zodiac sign Scorpio")
elif ((cust_birth["month"] == 11) and (cust_birth["day"] in range(23,31,1))) or ((cust_birth["month"] == 12) and (cust_birth["day"] in range(22))):
    print ("Your zodiac sign Sagittarius")
elif ((cust_birth["month"] == 12) and (cust_birth["day"] in range(22,32,1))) or ((cust_birth["month"] == 1) and (cust_birth["day"] in range(21))):
    print ("Your zodiac sign Capricorn")

