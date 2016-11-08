import sys

my_file = open ('file.txt', 'w')

print("process started! ")

name = print(input("what is your name dude? :"))
age = print(input("how old are you? :"))
email = print(input("pelase enter your email :"))

my_file.write ("Hello , now you see my name , age , and ( email ) \r\n")
my_file.write ("bye all , nice to meet you !")

print("process finished, bye! ")

my_file.close()

