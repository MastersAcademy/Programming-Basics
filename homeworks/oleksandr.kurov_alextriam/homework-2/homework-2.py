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
print ("Dictionary, key and value: ", dict1)
# print only values
print ("Dictionary only values: ",dict1.values())

# lists
listName=list (name + lastName)

print ("List exsample:", listName)

#write dictionary in file
filename=name+'_'+lastName+".csv"
f = open(filename,'w')
data_to_write=str(dict1)+'\n'
f.write(data_to_write)
f.close