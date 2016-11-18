name = input("Please enter your name:")
last_name = input("Please enter you last name:")
age = int(input("Please enter your age:"))

hello_text = "Your name is %s %s. You are %i years old. Nice to meet you, %s!" %(name, last_name, age, name)
myfile = open("hello.txt", "w")
myfile.write(hello_text)
myfile.close()

myfile = open("hello.txt", "r")
print("----Reading new file----")
print(myfile.read())
myfile.close()


