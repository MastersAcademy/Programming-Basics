print (9**19 - int(float(9**19)))

# put your python code here
sleepMinute=int(input())
hour=int(input())
minute=int(input())

sleepHour= sleepMinute //60
sleepMin= sleepMinute % 60

print (sleepHour+hour)
print (minute+sleepMin)