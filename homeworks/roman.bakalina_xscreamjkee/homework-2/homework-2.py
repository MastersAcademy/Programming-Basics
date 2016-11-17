#!/usr/bin/env python3
print("\n     	 homework-2")
print("\n>>Create file and enter some information <<\n")

#entering information
f_name = input("Enter the file name: ")
f_name = f_name+".txt"
print("\n>>Your file is created: ",f_name)

coll = {}
coll['word'] = input("\nEnter a word or phrase that you want add to the your file: ")
coll['name'] = input("\nEnter your nickname or name: ")
coll['age']  = input("\nEnter your age: ")
coll['country'] = input("\nEnter your country: ")

info = "\nSome of the information you entered:\nWord: %s\nNickname: %s\nAge: %s\nCountry: %s"%(coll['word'], coll['name'], coll['age'], coll['country'])
print(info)

#write text on file
f_txt = open(f_name,'w')
f_txt.write(info)
f_txt.close()
print(">>Your file is saved.<<\n")

#exit
input("Press 'Enter' to exit:")
print("\nGoodbay,",coll['name'])