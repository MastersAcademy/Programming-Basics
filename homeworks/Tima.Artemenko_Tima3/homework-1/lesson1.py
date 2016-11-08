print("process Started")

name = input("Enter your name:")
surname = input("Enter your surname:")
age = int(input("Enter your age:"))
city = input("What is your city?:")
hometown = input("Where are you from?:")

own_text = "Your name is %s %s\n You are %i years old\n Your city is %s\n You are from %s!" %(name,surname,age,city,hometown)#thats all will be seen in txt file !

my_file = open("own.txt", "w") #opend a file txt!
my_file.write(own_text)
my_file.close() #closed a file!

print("process Finished, bye")