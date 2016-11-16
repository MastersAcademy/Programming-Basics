#!/usr/bin/env python3

print("\n     	 homework-1")
print("\n>>Create file and enter text.<<\n")

#entering information
f_name = input("Enter the file name: ")
f_name = f_name+".txt"
print("\n>>Your file is created: ",f_name,"\n")
word = input("\nEnter a word or phrase that you want add to the your file: ")
name = input("\nEnter your nickname or name: ")


#write text on file
f_txt = open(f_name, 'w')
f_txt.write(word + "\n")
f_txt.write(name + "\n")
f_txt.close()


#read text from file
print("\n>>Text that you added to file:\n")
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