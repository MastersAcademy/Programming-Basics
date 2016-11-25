name = str(input("What is your name?"))
print ("Hello, " + name + "!!!")
start = input("Would you like to answer some questions?")

if start == 'yes':
    print ("Ok, let's go!")
    surname = input("What is your surname?")
    birth = input("What is your date of birth?")
    adress = input("Where are you from?")
    print ("Thank's for information! Good buy!")
    
else:
    print ("It's a pity, good buy!")


f = open('D:\LearningPython\saveName.txt','w')
f.write (name)
f.write (surname)
f.write (birth)
f.write (adress)
f.close ()
