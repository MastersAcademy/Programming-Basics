import datetime

print('---///Python Super Data Collector 3000 v1.0\\\---')

visitor = {}

visitor['name'] = str(input('Please, enter your (or not your) name for program testing: '))
visitor['planet'] = str(input('Enter your current location planet: '))

with open('visitors.txt', 'a') as file:
    now = datetime.datetime.now()
    file.write(now.strftime('%d-%m-%Y %H:%M:%S') + '\t' + visitor['name'] + ' : ' + visitor['planet'] + '\n')

print(('\n' + 'Greetings %s from %s!' + '\n' + 'Data stored without your agreement!' + '\n' + 'Bye!') % (visitor['name'],visitor['planet']))


