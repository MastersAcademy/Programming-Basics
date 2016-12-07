print("If you want to study in Masters Akademy, you must fill the form")


name = input ("What is your name?")
surname = input ("What is your surname?")
age = int(input ("How old are you?"))
if age >= 18:
  print 'this is a good age to start IT careers'
else:
  print 'Sorry, come when you turn 18'
adress = input("Where do you live?")
name_surname = name+' '+surname


answer = "Hello, thank you %s, your age is %i it is a good age to start a career in IT in %s" % (name_surname, age, adress)

print(answer)

Anketa = open("Anketa.txt", "w")
Anketa.write(answer)
Anketa.close()

#List
Anketa = open("Anketa.txt", "w")

List_a = [name+' '+ surname, age, adress]
print (List_a)


Anketa.write('[]'.format(List_a))
Anketa.close()




