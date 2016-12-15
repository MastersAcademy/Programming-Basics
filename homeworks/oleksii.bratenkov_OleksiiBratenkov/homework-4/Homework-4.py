
print ("Hello! Can I ask you a few questions?")
name = input("What is your name? ")
city = input ("Where are you live? ")
age = int(input("What is your age? "))

if age in range (0, 17):
    print ("You are child!")
elif age in range (17,55):
    print ("You are adult!")
else:
    print ("You are old!")


dict_a = {
    "name": name,
    "city":city,
    "age": str(age)
}
print (dict_a["name"])
print (dict_a)
answer = ("Hello, %s from %s, why you only %i ?" %(name, city, age))
print(answer)
print ("Hello" + ", " + dict_a["name"] + " you are so beatiful in your " + dict_a["age"] + " good luck you in " + dict_a["city"]) 



file = open ("answers.txt", "w")
file.write(answer)
file.close()
