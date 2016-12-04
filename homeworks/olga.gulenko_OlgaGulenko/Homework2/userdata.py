print('Hello! You  must enter some personal data.')
fileName = 'data.txt'
accessMode='w'

dict_user = {
    'name': input ('Your full name'),
    'mobile': int(input('Phone')),
    'address': input('Home address'),
    'email': input('e-mail'),
    'day': int(input('Number of desirable day of delivery(1-7)'))
}
if dict_user['day'] > 4:
    courier = ('The contact information of courier are: name - Andrev, phone - 093576555757.')
else:
    courier = ('The contact information of courier are: name - Ivan, phone - 093566788900.')
resultA = "Dear %s, tomorrow your parcel will be delivered to the address %s.\n" % (dict_user['name'],dict_user['address'] )
resultB = "We will send you the message to mobile %i or e-mail %s with the exact time of delivery.\n" % (dict_user['mobile'],dict_user['email'] )
resultC = "You chose day of delivery %i. %s" % (dict_user['day'], courier)
print(resultA)
print(resultB)
print(resultC)
File = open(fileName,accessMode)
File.write(resultA)
File.write(resultB)
File.write(resultC)
File.close()
print('Our congratulations!')
