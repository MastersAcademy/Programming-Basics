
print ("Hello , answer for some questions ")

name = input('Enter your name:')
last_name = input ("Enter your last name:")
age = input ('Enter  your age:')
city = input ('Where do you live?')



print('Thanks for your answer')
print(' name: %s\n last_name: %s\n age: %s\n city: %s' % (name,last_name,age,city))

f = open('results.txt', 'w')
f.write("name: " + name + '\n')
f.write("last_name: " + last_name + '\n')
f.write("age: " + str(age) + '\n')
f.write("city: " + city + '\n')
f.close()

if age in range(1,17):
     print("You are not adult")
elif age in range(18,125):
     print("You are adult")


d={}
d["name"] = name
d["last_name"] = last_name
d["age"] = age
d["city"] = city
print("Preview of Dictionary with user results")
print(' ')
print(d)

f = open('results.txt', 'a')
f.write("Dictionary" + '\n')
f.write(str(d))
f.close()

