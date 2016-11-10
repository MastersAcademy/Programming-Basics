f = open('questionnaire.txt', 'w')
# Ім'я
First_Name=str(input("Tell me please your first name: "))
print(First_Name+'\n')
f.write("First name: "+First_Name+'\n')

#Прізвище
Second_Name=str(input("Tell me please your second name: "))
print (Second_Name+'\n')
f.write('Second name: '+Second_Name+'\n')

#Розмір взуття
Size_footwear=str(input("Tell me please your shoe size: "))
print(Size_footwear+'\n')
f.write('Size footwear: '+'\n')

#Номер вашої банківської карти)
Bank=str(input('Tel me plese number of your bank card): '))
print(Bank+'\n')
f.write('Your number card: '+'\n')

#вік
Age=str(input("How old are you: "))
print(Age+'\n')
f.write("Age: "+Age+'\n')

#Улюблена марка телефона
Telephone=str(input('Who is the favorite brand please phone: '))
print(Telephone+'\n')
f.write('Favorit phone: '+'\n')

f.close()