import collections

# Application for collecting personal details for flight company


# Collecting personal data from client and storing it in Ordered Dictionary
personalData = collections.OrderedDict()
print('--- Someone will get to you shortly. Please Stand By ---')
personalData['name'] = str(input('Please state your full name: ')).title()
doublePrice = 0
for i in personalData['name'].split():
    if i == 'Donald':
        print("We are sorry to inform you but all clients with the name Donald must pay double price.")
        doublePrice = 1
        break
    elif i == 'Hillary':
        print("Lady, you are not better. Price doubled")
        doublePrice = 1
        break
    else:
        pass   # TODO Add some greetings to the approved client in text form


personalData['age'] = int(input('How old are you? '))

personalData['address'] = str(input('Where you do you live? ')).title()
print('Let me pronounce your address, to be sure we get it right: ')
symbol = 0
while symbol < len(personalData['address']):
    print("'%s'" % personalData['address'][symbol])
    symbol += 1


addressVerification = str(input('Please confirm your address, y/n'))
if addressVerification.capitalize() == 'Y':
    print('Proceed to the next question')
elif addressVerification.capitalize() == 'N':
    personalData['address'] = str(input('Repeat your address')).title()
else:
    print('You typed something gibberish. Proceed')


personalData['dest'] = str(input('Where are you heading? ')).title()

# Saving in variable and showing formatted data to the client
summaryMessage = ' Name: %s\n Age: %s\n Home address: %s\n Destination: %s'\
                 % (personalData['name'], personalData['age'], personalData['address'], personalData['dest'])
print(summaryMessage + '\n Thank you for your time ')

