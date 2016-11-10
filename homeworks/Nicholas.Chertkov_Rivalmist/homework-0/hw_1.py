print("\n auto(1) or hand write(2)".title())

auto = input("\n1 or 2: ")
# auto
if auto == "1":
	print("\n\tName: Nicholas\n"
		  "\tSurname: Chertkov\n"
		  "\tAge: 20\n")
# 	auto

# hand_write
elif auto == "2":
	print("Your name: ")
	name = input("\n")
	print("\t" + name.title())

	print("Your surname: ")
	surname = input("")
	print("\t" + surname.title())

	print("Your age: ")
	age = input ("")
	print("\t" + age)
# hand_write

# if  mistake in 1/2
else:
	print("Error. Try again")
# if  mistake in 1/2