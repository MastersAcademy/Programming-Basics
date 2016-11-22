f = open("homework1vasya.txt",'w',encoding="utf8")

name = input("What is your name? ")
print("Hi", name)
age = int(input("How old are you?"))
print("Cool!", age)
hair =input("What is your colour hair?")
eyes = input("What is your colour eyes?")

acquaintance = ("Ah, so your name is %s, your age is %i,your eyes is %s, "
"and you colour hair %s. Fantastic! Go to the bar." % (name, age, eyes, hair))
print(acquaintance)

f.write(acquaintance + "\n")
f.close()

list_a = []
list_a.append(name)
list_a.append(hair)
list_a.append(hair)
list_a.extend(eyes)

print (list_a)


list_b = list(name)

print(list_b)

list_c =[list_a,list_b,age]



print(list_c)

set_a = set(list_a)

print(list(set_a))


dict_a ={"name":name,"eyes":age}




dict_b = {"city":hair, "work":eyes}
print(dict_b)

dict_c = {"about":dict_a, "beaut":dict_b}


print(dict_c)
