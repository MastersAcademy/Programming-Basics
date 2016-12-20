import random

print('Hi, please input information about you')

name = input('What is your name?\n')
while not name:
    name = input('Please, input your name\n')


surname = input('What is your surname?\n')
while not surname:
    surname = input('Please, input your surname\n')


age = input('How old are you?\n')
while (age.isdigit()!=True):
    print('Age must be digit')
    age = input('Please, input your age\n')


city = input('Where are you live?\n')
while not city:
    city = input('Please, input city where you live\n')
    

email = input('What is your e-mail?')
while not email:
    email = input('Please, input your e-mail\n')


phone = int(input('What is your phone?'))
while not phone:
    phone = input ('Please< input your phone\n') 


#print('=======_RESULT_=======')
#result = ("Your name is %s %s, you are %i years old,you live in %s,and your contact information is:\n e-mail: %s \n phone: %i" % (name,surname,age,city,email,phone))
#file = open('bio.txt','w')
#file.write(result)
#file.close()
#print (result,'\n','All information saved,thank you')

##############################################################

print ('======== Homework 3 ========')

bio_info=[]
bio_info.append(name)
bio_info.append(surname)
bio_info.append(age)
bio_info.extend(city)
bio_info.append(phone)
bio_info.append(email)

print (bio_info)
del bio_info[3]
bio_info.pop()
print (bio_info)

list_for_sort = [10,1,9,2,8,3,7,4,5]
print (sorted(list_for_sort))
print (list_for_sort)
list_for_sort.sort()
print (list_for_sort)

list_for_set = [300, 'Spartans', 'eats', 600, 'kebabs']
print (list_for_set)
set_a = set(list_for_set)
print (set_a)

dict_bio = {
    'first name': 'Vladislav',
    'second name': 'Kim',
    'date': '20-09-1995'
}
print (dict_bio)

dict_city_visited = {
    'Lviv':{
        'rate': '8/10',
        'where been': 'Zamkova mountain'
    },
    'Kyiv':{
        'rate': '7/10',
        'where been': 'Independance Square'
    },
    'Zhitomyr':{
        'rate': '10/10',
        'where been': 'Military procuracy'
    }
}

dict_bio['city visited'] = dict_city_visited
print (dict_bio)

####################################################################

print ('==========_HOMEWORK_4_==========\n')
game_1 = input('Lets play a game? Y/N\n')
while (game_1 != 'N') and (game_1 !='Y'):
    game_1 = input('You must say Yes(Y) or No(N)\n')


if game_1 == 'Y':
    player = int(input('Input number in range 1..100\n'))
    while (player<0) or (player>100):
        player = int(input('Just input number in range 1..100\n'))
   

    rund_numb = random.randint(1,100)
    if player > rund_numb:
        print('You WIN! Your number %i bigger then my number %i' %(player,rund_numb))
    elif rund_numb > player:
        print('I WIN! My number %i bigger then your number %i' %(rund_numb,player))
    else:
        print('Its a DRAW! My number %i = your number %i' %(rund_numb,player))

                         
if game_1 == 'N' :
    print('Its sad(')


for x in range(-10,10):
    if x<0:
        print(x)        
        break
    else:
        print ('finish without break')


for x in range(-10,10):
    if x<6:
        continue
    print ('continue %i' %x)


for x in range(1,5):
    if x<3:
        pass
    print ('pass %i' %x)    