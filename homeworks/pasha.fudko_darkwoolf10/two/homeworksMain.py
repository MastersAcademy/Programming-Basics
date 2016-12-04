name = input("What is your name? ")
surname = input("your surname? ")
age = int(input("How old are you? "))
dateOfBirth = input("Enter your date of birth? ")
city = input("Where do you live? ")

print("Your surname sounds good - %s, and your name is beautifu, %s "
      "you have born in %s,so you %i years old now, "
      "and you live in the most interesting place what call %s" % (surname, name, dateOfBirth, age, city))

f = open('date.txt', 'w')
f.write('name - ' + name + '\n')
f.write('surname - ' + surname + '\n')
f.write('age - ' + str(age) + '\n')
f.write('date of birth - ' + dateOfBirth + '\n')
f.write('city - ' + city)
f.close()
