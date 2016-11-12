print ("Hello friend!")
name = str(input ("What is your name? "))
surname = input ("What is your surname? ")
age = int(input("How old are you? "))
city = input ("Where do you live? ")

result = ("So your name is %s %s, and you are %i years old. "
       " %s is qreat city!" % (name, surname, age, city))
print (result)

file = open ("info.txt", "w")
file.write(result)
file.close()
