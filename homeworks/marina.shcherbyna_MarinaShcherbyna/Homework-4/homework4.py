#!/usr/bin/env python3
print ("Hello! Welcome to our game!")
print ("")
name = str(input ("What is your name?"))
nickname = str(input ("What is your best feature you like?"))
place = str(input ("What is your favourite country?"))
gender = str(input ("What is your gender? (m/f)"))
if gender == 'm':
    gen = ("Sir")
elif gender == 'f':
    gen = ("Miledy")
else:
    gen = ("crazy")

print ("")
print ("We congratulate you, "+gen+" "+name+" "+nickname+" from the "+place+"!")
print ("")
print ("Please, check the info")
list1 = [gen, name, nickname, place]
for i in list1:
    print ('-' + str(i))
print ("")

print ("Your scared servants from Africa will call you the next way.....")
all = (gen, name, nickname)
for i in all: print (i * 2, end='')


print ("")
print ("Your dog will call you the next way.....")
for i in all: print ("Gaff gaff gaff", end='')


print ("")
age = int(input ("How old are you?"))
while age <= 14:
    print ("This game have bloody scenes. Go and do your homework!")
else:
    print ("Have fun!")
print ("")
print ("")
print ("Dear " + gen +" " + name +" " + nickname +" from the " + place + " ! You are the Lord of very rich castle! You have a lot of servants, your fields are full of harvest, your bank is full of money, your daughter is the most beautifil in the world. But once an evil Dragon have stolen your daughter. You are trying to resque her.")
choise1 = str(input ("You are leaving the castle and go ahead to the crossroad. What way will you chose: Left (L), Straight(S), Right(R) or Back(B)?"))
print ("")
if choise1 == "L":
    print ("You came to the river. The waves are very big, it is stormy. You are going to swim to the opposite side. You swim good, but storm is very strong. Your people saved you, but your daughter is lost")
    print ("Try again later!")
elif choise1 == "S":
    print ("You came straight and see a big castle. It is bigger than yours. You came into and forgot your daughter. The witch are leaving here and she are going to eat you.")
    print ("Try again later!")
elif choise1 == "R":
    print ("You came to the Dragon cave. After heavy battle you beated the Dragon and saved your daughter!")
    print ("You are the champion!!!!")
elif choise1 == "B":
    print ("Are you sure? Your daughter is in danger!")
    print ("Try again later!")
else:
    print ("You are not serios! Your kingdom is in danger!!!")


input ("Press Enter to finish")