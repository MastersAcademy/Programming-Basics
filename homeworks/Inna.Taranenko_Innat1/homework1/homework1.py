name = input("What is your name?")
print ("Hello, " + name + "!!!")

surname = input("What is your surname?")
birth = input("What is your date of birth?")
adress = input("Where are you from?")
print ("Thank's for information! Good buy!")

textdoc = name +" " + surname + " was born in " + adress + " in " + birth
print (textdoc)

f = open('D:\LearningPython\saveName.txt','w')
f.write (textdoc)
f.close ()
