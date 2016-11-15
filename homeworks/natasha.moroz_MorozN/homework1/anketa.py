print ("Hello! by filling out a simple form to continue using the site.")

anketa = open("anketa.txt", "w")

name = input ("What is your name?")
surname = input ("What is your surname?")
age = int(input ("How old are you?"))
town = input ("Where do you live?")
name_surname = name + ' ' + surname

letter = "Thank you %s, your age is %i you can continue to work with databases %s" % (name_surname, age, town)

print(letter)

anketa.write(letter)
anketa.close()
