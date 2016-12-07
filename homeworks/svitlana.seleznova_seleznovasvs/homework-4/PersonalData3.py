print("Hello! Please, enter your personal data.")
name = input("What is your name? ")
surname = input("What is your surname? ")
age = int(input("How old are you? "))
if age < 18:
    print("Under age 18!!! Access denied")
    quit()
else: print("Let's write more information")
mobile = int(input("Telephone number: "))
address = input("Enter your home address: ")
email = input("E-mail: ")
print("Congratulations!!! Dear %s, thank you for registering on our website.\n We will send you the message to mobile %i or e-mail %s with your entering data.\n WELCOME!" % (name, mobile, email))

list_person = [name, surname]
list_data = [mobile, address, email]
list_person_data = [list_person, list_data]

for x in list_person:
    print(x, len(x))
    
print (list_person)
print(list_data)
for i in range(len(list_data)):
    print(i, list_data[i])

print(list_person_data)

dict_person = {
    "name": name,
    "surname": surname,
    "age": age,
    "email": email,
}
print(dict_person)

