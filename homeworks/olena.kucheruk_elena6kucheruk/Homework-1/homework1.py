print ("Please write about your favorite books \n")

name = input("What is your name?\n  ")
age = int(input("What is your age?\n    "))
book = input("What is your favorite book?\n         ")


#results
result = ("Your name is %s, You are %i years old, your favorite book is %s. Thank you." % ( name, age, book ))
print (result)

#save
f= open ('results.txt', 'w')
f.write (result)
f.close ()
