name = input ("please enter your name ")
address = input ("please enter your address ")
age = int(input("please enter your age "))

if age in range (0, 17):
    print (" You are child!")
elif age in range ( 18, 55):
    print (" You are adult!")
else :
    print (" You age old")
    

dict_a = {
    "name" : name,
    "age" : str(age),
    "address" : address
}

answers = (" Hello" + ", " + dict_a["name"] + " your age is " + dict_a["age"] + " and you live in " + dict_a["address"] + ".")
print (answers)
answers2 = ("Hello, %s , why you so young in %i and you live here - %s" %(name,age,address))
print (answers2)
file = open("answers.txt", "w")
file.write(answers)
file.write(answers2)
file.close()
