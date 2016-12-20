print ("Hello i want ask you something. Are you ok whith this? y/n")
Helo_answer=str(input())
false=(str("n"))
true=(str("y"))
if Helo_answer==(false):
    print ("Ok! No problem! Bye!")
    quit()
if Helo_answer==(true):
    print ("OK! Lets start")
    print ("What is your name?")
    name=str(input())
    print ("What is your second name?")
    second_name=str(input())
    print ("How old are you?")
    age=int(input())
    print ("Where are you from?")
    city=str(input())
    print ("Lets check your answers")
    correction=("You are -" + name +"." +
            "Your second name is " + second_name + "." +
            "You are from " + city + ".")
    print (correction)
    print ("Oh!just forget. You are %i years old" %(age) )
    print ("Is this correct answers? y/n")
    correct_answer=str(input())
    if correct_answer==false:
        print ("You need to change your answers,please,start this programm again and change them")
        quit()
    if correct_answer==true:
        file = open("saved_data.txt","w")
        file.write("Name - %s, Second name - %s, age - %i, City - %s, \n"%(name,second_name,age,city))
        file.close()
        print("Thanks! I saved your data to file")
else: print("Please answer y/n")


print("Lets have more data from you")


#Collection
list_privateinfo=[]
Email=input(str("Enter your email please: "))
list_privateinfo.append(Email)
Phone=input(str("Enter your phone please: "))
list_privateinfo.append(Phone)
Hobby=input(str("Enter one your hobby please: "))
list_privateinfo.append(Hobby)
print(list_privateinfo)
print("Lets make your phone number more secure")
del list_privateinfo[2]
list_privateinfo.pop(1)
list_privateinfo.extend(Phone)
list_privateinfo.append(Hobby)
print(list_privateinfo)

print("Lets save these data to the file")
file = open("saved_data.txt","a")
file.write("\n".join(list_privateinfo))
print("Successfully saved")#

    #Dictionary
print("Lets add more data in other format")
dict_data={}
wife_name=input(str("Enter your wife`s name please: "))
dict_data['wifes_name']=wife_name
wife_dob=input(str("Enter your wife`s date of birth please: "))
dict_data['wifes_dob']=wife_dob
son_name=input(str("Enter your son`s name:"))
dict_data['sons_name']=son_name
sons_dob=(input(str("Enter your son`s date of birth:")))
dict_data['sons_dob']=sons_dob

print("Lets save these data to the file")
import json
with open("saved_data.txt","a") as f:
    json.dump(dict_data, f)
print("Data was successfully saved. Thanks")


#Control Flow
print("Lets Play with IF and ELSE and RANGE")
print("How old are you?")
ages=int(input())
if ages in range(0,2):
    print("Oh you are baby!")
elif ages in range(2,14):
    print("You are child!")
elif ages in range(14,21):
    print ("You are teenager!")
elif ages in range(21,30):
    print ("You are young!")
elif ages in range(30,45):
    print ("You are adult")
else:
    print("You are old!")
# (WHILE)
print("Lets count your age")
Age_counter=0
while Age_counter <= int(ages - 1):
    Age_counter +=1
    print(Age_counter)


print("Lets show your age with a help of CONTINUE")
Age_counter_2=0
while Age_counter_2 <= int(ages - 1):
    Age_counter_2 += 1
    if Age_counter_2 < int(ages):
        continue
    elif Age_counter_2==int(ages):
        print(Age_counter_2)


quit()
