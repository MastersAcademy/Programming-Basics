print("For registration you need to answer a few questions:")

account = { }
account["first_name"] = input("What is your Name?")
account["last_name"] = input ("What is your Last Name?")
account["age"] = int(input("How old are you?"))
if account["age"] <= 18:
	print("We are sorry, you're too young")
else:
	account["email"] = input("Please, enter your email")
	account["password"] = input("Pleasee, enter your password")
	print("Thank for your answers. Whait a moment please")
	result = ("Your name is %s %s, you are %d years old, your email is: %s and you are password is: %s" % (account['first_name'], account['last_name'], account['age'] , account['email'], account['password']))
	f = open("account.txt", "w")
	f.write(result)
	f.close()

        print(result)
        print("Please, wait a moment")
        print("Loading...")
        i = 5
        while i > 0:
            print(i)
            i = i - 1
        else:
            print("We welcome you on our service!")