import collections

# Application for collecting personal details and saving them in a file.


# Collecting personal data from client and storing it in Ordered Dictionary
personalData = collections.OrderedDict()
print('--- Someone will get to you shortly. Please Stand By ---')
personalData['name'] = str(input('Please state your full name: ')).title()
personalData['age'] = str(input('How old are you? '))
personalData['address'] = str(input('Where you do you live? ')).title()
personalData['dest'] = str(input('Where are you heading? ')).title()

# Saving in variable and showing formatted data to the client
summaryMessage = ' Name: %s\n Age: %s\n Home address: %s\n Destination: %s'\
                 % (personalData['name'], personalData['age'], personalData['address'], personalData['dest'])
print(summaryMessage + '\n Thank you for your time ')

# Writing data in file
file = open('personal-data.txt', 'w')
for k, v in personalData.items():
    file.write(k + ': ' + v + '\n')
file.close()
