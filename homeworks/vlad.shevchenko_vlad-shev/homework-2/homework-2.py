name = str(input("What is your name?\n"))
surname = str(input("Your surname ?\n"))
age = int(input("How old are you?\n"))

data = {
	"Name":name,
	"Surname":surname,
	"Age": str(age)
}
print("Name: "+name+"\nSurname: "+surname+"\nAge: "+str(age))

file = open("aboutuser.txt", "w")

for key, item in data.items():
	file.write(key+":"+item+"\n")

file.close()
