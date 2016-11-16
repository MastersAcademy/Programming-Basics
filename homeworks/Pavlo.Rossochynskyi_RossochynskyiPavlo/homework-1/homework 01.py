# statistical data
name = input("What is your name?")
last_name = input("What is your last name?")
age = int(input("What you age?"))
adress = input("What is your email address?")
text = ("Hello, %s %s. We welcome you to our survey!" % (name, last_name))
print(text)

# file
my_file = open("Hello.txt", "w")
my_file.write(text)
