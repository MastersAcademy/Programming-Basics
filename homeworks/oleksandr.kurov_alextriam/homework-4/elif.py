#homework-2
name = input("What is your name? ")
lastName = input ("What is your lastname? ")
age = int(input("How old are you? "))
country = input("Where do you live (country)? ")

dict1= {'Name': name,
        'Last Name': lastName,
        'age':age,
        'country':country}#

# print all keys and values
#print ("Dictionary, key and value: ", dict1)
# print only values
#print ("Dictionary only values: ", dict1.values())

# homework-4

if len(name) < 2:
    print ('Name too short!')
elif len (name) > 2 and len (name) < 10:
    print ('Your name is normal leihgt')
else:
    print ('Your name is too long!!!')


for w in name:
    if w=='a' or w=='A':
        print ("Name content letter A or a!")
        break
else:
    print("Name not content letter a")

i=0
while i < age:
    print (i)
    i=i+1








