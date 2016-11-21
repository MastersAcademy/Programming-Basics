name = input("Please enter your name:")
last_name = input("Please enter you last name:")
age = input("Please enter your age:")

dict_data = {
    'name': name,
    'last_name':last_name,
    'age': age
}

hello_text = "Your name is %s %s. You are %s years old. Nice to meet you, %s!" %(dict_data["name"], dict_data["last_name"], dict_data["age"], dict_data["name"])
myfile = open("hello.txt", "w")
myfile.write(hello_text)
myfile.close()

print(hello_text)


