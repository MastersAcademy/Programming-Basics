#!/usr/bin/env python3
print ("Hello! We will create your CV online")
print ("-------Personal information---------")
item = []
name = str(input ("What is your name?"))
surname = str(input ("What is your surname?"))
dob = str(input ("When were you born?"))
address = str(input ("Where do you live?"))
all = (name,surname,dob,address)
item = [all]
print ("---------Please check your personal information----------")
print (item)
print ("Please, write your profession")
profession = str(input ("What is your profession?"))
item.append(profession)
print (item)
print ("----------OK! Now we will add this information to the data base------------")
dict = {"name":name, "surname":surname, "dob":dob, "address":address, "profession":profession}
print (dict)
print ("----------The last question and then we*ll finish-------------")
phone = str(input ("What is your phone number?"))
education = str(input ("What university you graduated?"))
dict_1 = {"phone":phone, "education":education}
print (dict_1)
dict["additional information"] = dict_1
print ("----------Your CV is in our data base. We will call you----------")
print (dict)

file = open ("homework2.txt", "w")
file.write(str(dict))
file.close()

input ("Press Enter to finish")