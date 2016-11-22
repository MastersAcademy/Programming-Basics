print("Hello! Please, enter your personal data.")
fileName = "PersonalData2.txt"
accessMode="w"
name = input("What is your name? ")
surname = input("What is your surname? ")
age = int(input("How old are you? "))
mobile = int(input("Telephone number: "))
address = input("Enter your home address: ")
email = input("E-mail: ")
answer1 = ("Congratulations!!! Dear %s, thank you for registering on our website.\n" % (name))
answer2 = ("We will send you the message to mobile %i or e-mail %s with your entering data." % (mobile, email))
File = open(fileName,accessMode)
File.write(answer1)
File.write(answer2)
File.close()
print("Congratulations!!! Dear %s, thank you for registering on our website.\n We will send you the message to mobile %i or e-mail %s with your entering data.\n WELCOME!" % (name, mobile, email))

list_person = [name, surname, age]
list_data = [mobile, address, email]
list_person_data = [list_person, list_data]

print (list_person)

print(list_data)

print(list_person_data)

dict_person = {
    "name": name,
    "surname": surname,
    "age": age,
    "email": email,
}
print(dict_person)

