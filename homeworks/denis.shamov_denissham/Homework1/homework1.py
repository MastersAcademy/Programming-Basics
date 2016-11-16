print ("Hello i want ask you something. Are you ok whith this? y/n")
Helo_answer=str(input())
false=(str("n"))
true=(str("y"))
if Helo_answer==(false):
    print ("Ok! No problem! Bye!")
    quit()
if Helo_answer==(true):
    print ("OK! Lets start")
    print ("What is your name?")
    name=str(input())
    print ("What is your second name?")
    second_name=str(input())
    print ("How old are you?")
    age=int(input())
    print ("Where are you from?")
    city=str(input())
    print ("Lets check your answers")
    correction=("You are -" + name +"." +
                "Your second name is " + second_name + "." +
                "You are from " + city + ".")
    print (correction)
    print ("Oh!just forget. You are %i years old" %(age) )
    print ("Is this correct answers? y/n")
    correct_answer=str(input())
    if correct_answer==false:
        print ("You need to change your answers,please,start this programm again and change them")
        quit()
    if correct_answer==true:
        file = open("saved_data.txt","w")
        file.write("Name - %s, Second name - %s, age - %i, City - %s"%(name,second_name,age,city))
        print("Thanks! I saved your data to file")
        quit()


