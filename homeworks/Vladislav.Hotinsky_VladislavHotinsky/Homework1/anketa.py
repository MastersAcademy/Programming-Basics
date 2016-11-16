print("If you want to study in Masters Akademy, you must fill the form")

anketa = open("anketa.txt", "w")

name = input ("What is your name?")
surname = input ("What is your surname?")
age = int(input ("How old are you?")) 
adress = input("Where do you live?")
name_surname = name+' '+surname

answer = "Hello, thank you %s, your age is %i it is a good age to start a career in IT in %s" % (name_surname, age, adress)

print(answer)

anketa.write(answer)
anketa.close()

