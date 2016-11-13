name = raw_input ("Tell us your name. ")
where = raw_input("Where you came from, %s ? " %(name))
age = int(input("How old are you? "))

print ("I think we can find something for you.")

text = ("Name - %s.\nNative town - %s.\nAge - %i." %(name, where, age))

file = open("homework-1.txt", "w")
file.write(text)
file.close()