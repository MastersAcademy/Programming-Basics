#!/usr/bin/env python3

print("\n     	 homework-2")
print("\n>>Create file and enter some information in the dictionary<<\n")

#entering information
f_name = input("Enter the file name: ")
f_name = f_name+".txt"
print("\n>>Your file is created: ",f_name,"\n")
word = input("\nEnter a word or phrase that you want add to the your file: ")
name = input("\nEnter your nickname or name: ")
age  = input("\nEnter your age: ")
country = input("\nEnter your country: ")

#dictionary
diction = {
		"word or phrase": word,
		"name":name,
		"age":age,
		"country":country
		}

#write text on file
f_txt = open(f_name, 'w')
f_txt.write(str(diction))
f_txt.close()


#read text from file
print("\n>>Information that you added to file:\n")
f_txt = open(f_name, 'r')
line = f_txt.readline()
while line:
	print (line)
	line = f_txt.readline()
f_txt.close()
print("\n>>Your file is saved.<<\n")


#exit
input("Press 'Enter' to exit:")
print("\nGoodbay,",name)