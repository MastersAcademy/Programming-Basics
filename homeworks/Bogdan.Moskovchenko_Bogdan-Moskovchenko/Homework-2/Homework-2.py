#intro

print('Our WORLD OF SEACREATURES welcomes you newcomer')
print('This game is for people who loves to observe all kinds of seadwellers')
print('For yours and ours conveniece please input some personal information')

#request

name = input('What is your name?\n')
surname = input ('What is your surname?\n')
age = int(input('How old are you?\n'))
creature = input('What kind of seacreatures do you want to observe the most?\n')

#result

result = ("Your name is %s %s, you are %i years old and you are fond of %s" %(name,surname,age,creature))

#additional request

print('For better communication with our clients we would like to ask for some additional information')

hobby = input('what kind of hoobby do you have?\n')
pet = input('Do you have a pet?\n')
colour = input('what is your favorite colour\n')

#dictionaries

dict_a = {
    'Name' : name,
    'Surname' : surname,
    'Age' : age,
    'Creature' : creature
    }

dict_b = {
    'Hobby' : hobby,
    'Pet' : pet,
    'Colour' : colour
}

dict_a['additional information'] = dict_b

print(dict_a)

#save

f = open('Seatamers.txt', 'w')
f.write(result)
f.close()

print(result)
print(' We welcome you newcomer\n Your journey begins right now')