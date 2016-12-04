import datetime

print('---///Python Super Data Collector 3000 v1.0\\\---')

visitor = {}

while 1 < 2:
    visitor['name'] = str(input('Please, enter your (or not your) name for program testing: '))
    visitor['age'] = int(input('Enter your age: '))
    visitor['planet'] = str(input('Enter your current location planet: '))

    if visitor['name'] and (visitor['age'] or visitor['age'] <= 0) and visitor['planet']:
        break

if visitor['age'] in range(0, 7):
    print('Hi kid!')

elif visitor['age'] in range(7, 17):
    print('Hi schoolkid! No hanky panky here!')

elif visitor['age'] in range(17, 21):
    print('Adult movies are enabled')

else:
    print('Life is lived and turning back is absent :(')

with open('visitors.txt', 'a') as file:
    now = datetime.datetime.now()
    file.write(now.strftime('%d-%m-%Y %H:%M:%S') + '\t' + visitor['name'] + ' : ' + visitor['planet'] + '\n')

print(('\n' + 'Greetings %s from %s!' + '\n' + 'Data stored without your agreement!' + '\n' + 'Bye!') % (
    visitor['name'], visitor['planet']))
