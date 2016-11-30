# statistical data
name = input("What is your name?")
last_name = input("What is your last name?")
age = int(input("What you age?"))
adress = input("What is your email address?")
text = ("Hello, %s %s. We welcome you to our survey!" % (name, last_name))
print(text)
print('--- === *** === --- ')

# dictionarie
dict_a = {
    'Name' : name,
    'last name' : last_name,
    'Age' : age,
    'Adress' : adress
    }
print(dict_a)
print('--- === *** === --- ')

# list
list2 = {name, last_name, age, adress}
print(list2)