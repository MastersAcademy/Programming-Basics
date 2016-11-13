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