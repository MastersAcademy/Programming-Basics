#homework-1
name = input("What is your name? ")
last_name = input ("What is your lastname? ")
age = int(input("How old are you? "))
country = input("Where do you live (country)? ")

print("Your name and lastmane is %s %s, your age is %i, "
      "and you live in %s. Good!" % (name, last_name, age, country))

#write data in file
filename=name+'_'+last_name+".csv"
f = open(filename, 'a')
data_to_write=name+";"+last_name+";"+str(age)+";"+country+'\n'
f.write(data_to_write)
f.close