name = input ("please enter your name ")
age = int(input("please enter your age "))
address = input ("please enter your address ")
answers = ("Hello, %s , why you so young in %i and you live here - %s" %(name,age,address))

dict_a = {
    "name" : name,
    "age" : str(age),
    "address" : address
}
answers2 = ("Hello" + ", " + dict_a["name"] + " your age is " + dict_a["age"] + " and you live in " + dict_a["address"] + ".")
print (answers2) 
print (answers)
file = open("answers.txt", "w")
file.write(answers)
file.write(answers2)
file.close()
