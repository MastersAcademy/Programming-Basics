# so simple hometask

print("Please answer following questions");
full_name = input("Full name: ")
age = int(input("Age: "))
e_mail = input("E-Mail for lettering: ")
print("Here may be endless questionarie but that's anough for today");
print()

# string formatting template
human_friendly_string_template = """That guy name is %s.
Born in late %d year.
Now is %d years old.
You can E-Mail on %s"""

# calculating year of birth
current_year = 2016
year_of_birth = current_year - age

ready_string = human_friendly_string_template % (full_name, year_of_birth, age, e_mail)

print("Your data:", ready_string, sep="\n")

# kidding

print()
print("Saving your data to FBI, CIA etc...")

target = open("questionarie.txt", "w")
target.write(ready_string)
target.close();

print("Saved")
print("Bye")