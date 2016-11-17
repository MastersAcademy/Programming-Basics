print('Hi, please input information about you')

name = input('What is your name?')
surname = input('What is your surname?')
age = int(input('How old are you?'))
city = input('Where are you live?')
email = input('What is your e-mail?')
phone = int(input('What is your phone?'))

result = ("Your name is %s %s, you are %i years old,you live in %s,and your contact information is:\n e-mail: %s \n phone: %i" % (name,surname,age,city,email,phone))
file = open('bio.txt','w')
file.write(result)
file.close()
print (result,'\n','All information saved,thank you')

##############################################################

print ('======== Homework 2 ========')

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

