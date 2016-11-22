print("Hello!")

answer = 'n'
name = ''
age = ''
phone = ''
email = ''
place = ''
while answer != 'y':
    name = input("What is your name?")
    age = int(input("How old are you?"))
    phone = input("Tell me your phone number?")
    email = input("Input your email address: ")
    place = input("Where do you live?")
    print("Confirm your data:")
    print("Name: %s\nAge: %i\nPhone: %s\nEmail: %s\nPlace: %s\n" % (name, age, phone, email, place))
    answer = input("Is it right? (y/n)")

print("Good! Have fun and remember: we know your name and where you live.")

f = open('output.txt', 'w')
f.write("Name: %s\nAge: %i\nPhone: %s\nEmail: %s\nPlace: %s\n" % (name, age, phone, email, place))
f.close()
