print("precess Started")

name = input("what is your name?:")
age = int(input("how old are you ?:"))
city = input("where do you live :?")

output = ("your name is %s\n you are %i years old \n you are from %s\n " % (name, age, city))
print(output)

outFile = open('file.txt', 'w')
outFile.write(output)
outFile.close()

print("process Finished")
