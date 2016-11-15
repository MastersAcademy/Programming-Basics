#questions
name = str(input("Enter youre name: "))
surname = str(input("Enter youre surname: "))
age = int(input("How old are you? "))
city = str(input("Where do you live? "))
game = str(input("Enter your favorite game: "))

#output on display
t = ("Hello %s %s, You just %i years! I also live in the city %s. By the way, %s also my favorite game! " %(name, surname, age, city, game))
print(t)
#create file
file = open('account.txt', 'w')
file.write(t)
file.close()
