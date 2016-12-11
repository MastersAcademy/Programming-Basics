accept = input("Let's start")
if accept:
    name = str(input("What is your name?\n"))
    surname = str(input("Your surname ?\n"))
    age = int(input("How old are you?\n"))
    data = [name, surname, age]

    while not name:
        name = str(input("What is your name?\n"))

    if age < 18:
        print("You are too small for this shit")
    elif age > 100:
        print("WTF!!!?!?!")

    for thing in data:
        if not thing:
            print("I didn't get enough data")
            break

else:
    print("Good luck!")
