# User's profile

print('Hello.\nWe need more information about you.\nMay you answer some qustions?')

# Confirm agree
answer = input("Enter (y)es or (n)o: ")

if answer == "yes" or answer == "y" or answer == "ye":

    print("Good. Let\'s go")

    user_name = str(input("What is your name? ")).capitalize()
    user_surname = str(input('Whar is your surname? ')).capitalize()
    address = str(input("Where do you live? ")).capitalize()
    age = int(input("How old are you? "))

    # Write in file
    user_file = open("user_file.txt", "w")
    user_file.write("User Profile\n")

    user_info = "Name: %s \nSurname: %s \nAge: %s \nAddress: %s " % (
        user_name, user_surname, age, address)

    print(user_info)

    dict_user = {
        "name": user_name,
        "surname": user_surname,
        "address": address,
        "age": str(age)
    }
    print("And now we need you contact information")

    user_email = str(input("Please enter your email "))
    user_phone = int(input("Please enter you phone number "))

    dict_user["email"] = user_email
    dict_user["phone"] = str(user_phone)

    for k, v in dict_user.items():
        print(k + ": " + v)

    print(dict_user)

    print("Hello %s %s! \nThank you for your help" % (user_name, user_surname))

    user_file.write(str(dict_user))
    user_file.close()

elif answer == "no" or answer == "n":
    print("Thank you for your time")

else:
    print("Try again")
