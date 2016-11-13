# Check isnside file
right_now = input("Inside file write '1': ")
if right_now == "1":
    with open("data.txt") as file_object:
        about_1 = file_object.read()
    print("\n" + about_1.title())

print("\nRewrite text ")
hand_write_1 = input("\tYour name is: ")
hand_write_2 = input("\tYour nickname on GitHub is: ")
hand_write_3 = input("\tDo you like write code?: ")
hand_write_4 = input("\t1Mac or Linux or Windows you use?: ")

# open and write text in data.txt
filename = "data.txt"
with open(filename, 'w') as file_object:
    file_object.write("Your name is: " + hand_write_1 + "\n")
    file_object.write("Your nickname on GitHub is: " + hand_write_2 + "\n")
    file_object.write("Like or dislike: " + hand_write_3 + "\n")
    file_object.write("Your OS is: " + hand_write_4 + "\n")

with open("data.txt") as file_object:
    about_1 = file_object.read()


withdraw = input("\nCheck what we write in data.txt write '1': \n")

# check what we write in data.txt file
if withdraw == "1":
    print("\tYour name is: " + hand_write_1.title() + "\n"
          + "\tYour nickname on GitHub is: " + hand_write_2.title() + "\n"
          + "\tLike or dislike: " + hand_write_3.title() + "\n"
          + "\tYour OS is: " + hand_write_4.title() + " ")

# # withdraw what in data.txt file we were read
# elif withdraw == "2":
#     print("\tInside data.txt: " + "\n" + about_1.title())

# mistake "if != 1 or 2" so print this
else:
    print("Error. Try again.")