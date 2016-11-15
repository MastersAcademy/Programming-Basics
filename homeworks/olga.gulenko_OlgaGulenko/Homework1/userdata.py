print('Hello! You  must enter some personal data.')
fileName = 'data.txt'
accessMode='w'
name = input('Your full name')
mobile = int(input('Phone'))
address = input('Home address')
email = input('e-mail')
resultA = ('Dear %s, tomorrow your parcel will be delivered to the address %s.\n' % (name, address))
resultB = ('We will send you the message to mobile %i or e-mail %s with the exact time of delivery.' % (mobile, email))
File = open(fileName,accessMode)
File.write(resultA)
File.write(resultB)
File.close()
print('Our congratulations!')