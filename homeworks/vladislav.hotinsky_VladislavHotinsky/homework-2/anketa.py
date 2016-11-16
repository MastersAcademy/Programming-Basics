print("If you want to study in Masters Akademy, you must fill the form")


name = input ("What is your name?")
surname = input ("What is your surname?")
age = int(input ("How old are you?")) 
adress = input("Where do you live?")
name_surname = name+' '+surname





#List
list_a = open("list_a.txt", "w")
list_a = [name+' '+ surname, age, adress]
print (list_a)

list_a.write(list_a)
list_a.close()




