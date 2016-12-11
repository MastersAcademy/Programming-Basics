
name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 18:
    print(" Hi so yang genius")
elif age > 40:
    print("hi old school")
else: print("hi")


city = input("Where  you from? ")
work = input("Where you work?")

print("Aha, so your name, and you work at %s is %s, and your age is %i, "
"and you live in %s. great!" % (name, work, age, city))
my_File = open("homework1",'w+',1)
my_File.write("Dear" + name + "\n")
my_File.write("You work at" + work + "in" + city + "\n")
my_File.write("Your age" +str(age))
my_File.close()

list_1 = []
list_1.append(name)
list_1.extend(city)

list_2 = list(work)

list_3 =[list_1,list_2,age]

print('--- ===  from for  === ---')

for i in list_1:
    print(i)


print('--- ===  from for arr  === ---')
for_Arr = []
for i in range(0,len(list_1),2):
    for_Arr.append(list_1[i])


print(for_Arr)

print('--- ===  array  === ---')

print (list_1)

print(list_2)

print(list_3)

list_3.pop()
del list_3[len(list_3)-1]

print(list_3)


print('--- ===  while  === ---')
it = int
it =0
while 1:
    it += 1
    if it % 2 == 0:
        continue


    print(it)


    if it > 20:
        break





dict_1 ={"name":name,"age":age}
dict_2 = {"city":city, "work":work}
dict_3 = {"ident":dict_1, "about":dict_2}

print(dict_1)

print(dict_2)

print(dict_3)

