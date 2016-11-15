# Application for collecting personal details and saving them in a file.

# Collecting personal data from client
print('--- Someone will get to you shortly. Please Stand By ---')
fullName = str(input('Please state your full name: ')).title()
age = int(input('How old are you? '))
address = str(input('Where you do you live? ')).title()
destination = str(input('Where are you heading? ')).title()

# Saving in variable and showing formatted data to the client
personalData = ' Name: %s\n Age: %i\n Home address: %s\n Destination: %s' % (fullName, age, address, destination)
print(personalData + '\n Thank you for your time ')

# Writing data in file
file = open('personal-data.txt', 'w')
file.write(personalData)
file.close()
