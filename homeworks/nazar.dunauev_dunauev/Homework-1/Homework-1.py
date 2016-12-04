name = input("What's you name?")
surname = input("What's you surname?")
age = int(input("How old are you?"))
city = input("Where are you from?")

answer = ("So, your name is %s %s \nYour age is %i \nYou are from %s" % (name,surname,age,city))

print(answer)

f = open('base.txt','w')
f.write(answer)
f.close()
