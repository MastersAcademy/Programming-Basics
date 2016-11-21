print("Tell us about your parents please.")
fathers_name = input("What is the name of your father? ")
fathers_age = int(input("How old is he? "))
fathers_profession = input("What is your father's profession? ")
list_father = [fathers_name, fathers_age, fathers_profession]

mothers_name = input("What is the name of your mother? ")
mothers_age = int(input("How old is she? "))
mothers_profession = input("What is your mother's profession? ")
list_mother = [mothers_name, mothers_age, mothers_profession]

print("One more question about your father:")
fathers_nationality = input("what is nationality of your father? ")
list_father.append(fathers_nationality)

print("Thnk you! and the last question about your mother:")
mothers_hair = input("What is the colour of your mother's hair? ")
list_mother.append(mothers_hair)

print("Great!")
surname = input("Write the surname of your family ")+"o"
list_family = [list_father, list_mother]
list_family.extend(surname)
print(list_family)
list_family.remove("o")
print(list_family)

choise = str(input(print("Do you want to see how i study dictonaries? y/n ")))
if choise == "y":
    dict_father = {
        'name': fathers_name,
        'age': fathers_age,
        'profession': fathers_profession,
        'nationality': fathers_nationality
    }
    print(dict_father)

    dict_mother = {
        'name': mothers_name,
        'age': mothers_hair,
        'profession': mothers_profession,
        'hair': mothers_hair
    }
    print(dict_mother)

    dict_family = {
        'father': dict_father,
        'mother': dict_mother
    }
    print(dict_family)
    dict_family['surname'] = surname
    print(dict_family)
else:
    print("0k")
print("Tank you for attention)")