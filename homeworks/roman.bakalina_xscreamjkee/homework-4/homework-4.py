#!/usr/bin/env python3
#Test program. Creates a file and does some operations on it

import os


menu = None
while menu != 5:
	
	print("""
	***********************************

	  		Menu:

	  1 - Create new file.	
	  2 - Add text on file.
	  3 - Read text from file.
	  4 - Remove file.
	  5 - Exit.

	***********************************
			""")

	menu = int(input("\n\nSelect step: ")) 

	#Create file
	if (menu == 1):
		f_name = input("\nEnter the file name: ")
		if (os.path.isfile(f_name)):
			print("\n>>The file name already exists")
		else:
			f_name = f_name		
			f_txt = open(f_name, 'w')
			f_txt.close()
			print ("\n>>Your file is created",f_name,"\n")


	#Add text on file
	elif (menu == 2):
		f_name = input("Enter the file name : ") 
		if (os.path.isfile(f_name)):
			word = input("Enter a word or phrase that you want to add to the file: ")
			f_txt = open(f_name, 'a')
			f_txt.write(word + '\n')
			f_txt.close()
			print("\n>>Chenge added!")
		else:
			print("\n>>Wrong name. File not found!")

	#Read text.	
	elif (menu == 3):
		f_name = input("\nEnter the file name : ")
		if (os.path.isfile(f_name)):
			print("\nText:")
			f_txt = open(f_name, 'r')
			line = f_txt.readline()
			while line:
				print (line)
				line = f_txt.readline()
			f_txt.close()
		else:
			print("\n>>Wrong name. File not found!")

	#Remove file
	elif (menu == 4):
		rm_file = input("Enter the name of the file to delete : ")
		if (os.path.isfile(rm_file)):
			os.remove(rm_file)
			print ("\n>>File deleted. ")
		else:
			print("\n>>Wrong name. File not found!")

	#exit
	elif (menu == 5):
		print("\n>>Goodbye!")

	else:
		print("\nThis command is not available.\n")