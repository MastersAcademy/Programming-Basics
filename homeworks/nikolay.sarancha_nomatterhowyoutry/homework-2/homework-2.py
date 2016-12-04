data = {}

data["name"] = raw_input("Tell us your name. ")
data["where"] = raw_input("Where you came from? ")
data["age"] = raw_input("How old are you? ")

print ("I think we can find something for you.")

text = ("Name - %s.\nNative town - %s.\nAge - %s." %(data['name'], data['where'], data['age']))

file = open("homework-2.txt", "w")
file.write(text)
file.close()