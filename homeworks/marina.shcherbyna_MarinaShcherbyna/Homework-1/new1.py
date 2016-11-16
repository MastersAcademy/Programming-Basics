#!/usr/bin/env python3
print ("Hello! Ansver several questions please")
name = str(input ("What is your name?"))
surname = str(input ("What is your surname?")) 
age = str(input ("How old are you?"))
profession = str(input ("What is your profession?"))

print ("So, your full name is "+name+" "+surname+" , you are "+age+", your profession is "+profession+".") 


fullinformation = "So, your full name is "+name+" "+surname+" , you are "+age+", your profession is "+profession+"." 


file = open ("new1.txt", "w")
file.write(fullinformation)
file.close()
input ("Press Enter to finish")