##HomeWork-1/ Working with input/output and with File methods

print("Hello")
print("Tell about yourself")



# Input var
FirstName = input("Enter your FirstName:")
LastName = input("Enter your LastName:")
Place = input("Where are you from:")
Age = int(input("How old are you?"))
Hobby = input("What are you Like:")

# Printing results into command line
Result = ("\n %s %s, you are from %s.\n You are %i years old and you like %s" % (FirstName, LastName, Place, Age, Hobby))
print(Result)


##File methods
#create, open file in write mode
InputText = [FirstName, LastName, Place, Age, Hobby, Result]
with open('base.txt', 'w') as DBFile:
    for line in InputText:
            print(line, file=DBFile)

DBFile.close()
