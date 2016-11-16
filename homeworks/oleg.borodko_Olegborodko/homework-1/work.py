try:
    name=str(input("Please enter your name: "))
    year=float(input("Please enter your age: "))
except:
    print("You have error in your data")
else:
    year=str(year)
    print("Your name is-"+name)
    print("Your age is-"+year)

    try:
        file = open('history.txt', 'a')
        file.write("Name-"+name+"\n")
        file.write("Year-"+year+"\n")
        file.write('---\n')
    except:
        print("can not write to file")
    else:
        print("thank you, your data was recorded")
    finally:
        # this works in any case
        file.close()
