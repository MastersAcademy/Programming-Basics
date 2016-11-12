name = str(input("What is your name?\n"))
surname = str(input("Your surname ?\n"))
age = int(input("How old are you?\n"))


file = open("aboutuser.txt", "w")

file.write(name+"\n")
file.write(surname+"\n")
file.write(str(age)+"\n")
file.close()
