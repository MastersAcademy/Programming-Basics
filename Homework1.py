print('Our WORLD OF SEACREATURES welcomes you newcomer')
print('This game is for people who loves to observe all kinds of seadwellers')
print('For yours and ours conveniece please input some personal information')

name = input('What is your name?\n')
surname = input ('What is your surname?\n')
age = int(input('How old are you?\n'))
creature = input('What kind of seacreatures do you want to observe the most?\n')

result = ("Your name is %s %s, you are %i years old and you are fond of %s" %(name,surname,age,creature))
f = open('Seatamers.txt', 'w')
f.write(result)
f.close()

print(result)
print(' We welcome you newcomer\n Your journey begins right now')