data = {}
data["name"] = input("What is your name?")
data["surname"] = input("What is your surname?")
data["age"] = input("How old are you?")
data["profession"] = input("What is your profession?")
print(data)

file = open("data.txt", "wt")
data_list = "User data:\n name: %s\n surname: %s\n age: %s\n profession: %s" %(data["name"], data["surname"], data["age"], data["profession"])
file.write(data_list)

new_list =[]
new_list.extend(data["surname"])
print(new_list)
del new_list[4]
print(new_list)

new_set = set(new_list)
print (new_set)
print (new_set.__class__)


