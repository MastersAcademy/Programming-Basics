print("precess Started")

name = input("what is your name?:")
age = int(input("how old are you ?:"))
City = input("where do you live :?")

file_01 = ("your name is %s\n you are %i years old \n you are from %s\n " % (name, age, City))
print(file_01)

files = [name, age, City, file_01]
with open("file.txt", "w") as newfile:
    for file in files:
        print(file=newfile)
        newfile.write(file_01)

print("process Finished")
newfile.close()