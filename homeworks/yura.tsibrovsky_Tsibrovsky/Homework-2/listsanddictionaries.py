#! /usr/bin/env python
# -*- coding: utf-8 -*-
print("this program will collect your info and pull it into list :) \n" )
print("Enter your data, please \n")
	# data collection	
list_fio = []
name_string = raw_input("Name ")
list_fio.extend(name_string)
#fathersname_string = raw_input("Отчество ")
#list_fio.extend(fathersname_string)
surname_string = raw_input("Last name ")
list_fio.extend(surname_string)
    #age_integer = int(input("Ваш возраст "))
nationality_string = raw_input("Национальность ")
list_fio.extend(nationality_string)
    #taxid_integer = int(input("Индивидуальный налоговый номер "))
    #email_string = raw_input("электронный ящик ")
    #city_string = raw_input("Город проживания ") 
    # convert data into lists
print("that is how it looks if we make list of all your letters")
#text = text.decode('utf8')
print(list_fio)  
print("the ammount of symbols is ", len(list_fio))
print("Funny ? \n")
print("let's sort it ")
print(sorted(list_fio))
set_fio = set(list_fio)
print("let's  delete repetitions ")
print(set_fio)

dict_baseinfo = {
    'first_name': name_string,
    'last_name': surname_string,
    'nationality': nationality_string
}

print(dict_baseinfo)

print("Enter additional data, please \n")
hobby1_string = raw_input("Your main hobby, please ")
hobby2_string = raw_input("Your secondary hobby, please ")
dict_baseinfo['hobbies'] = [hobby1_string,hobby2_string]
print(dict_baseinfo)

print("\nDo you have bad habbits ?")
select_string = raw_input("y/n ") 
if select_string == 'y' :
	badhabbit1_string = raw_input("bad habbit № 1 ")
	badhabbit2_string = raw_input("bad habbit № 2 ")
	badhabbit3_string = raw_input("bad habbit № 3 ")	
	dict_badhabbits = {
    '1:': badhabbit1_string,
    '2:': badhabbit2_string,
    '3:': badhabbit3_string
	}
	dict_baseinfo['bad habbits'] = dict_badhabbits
else :
	print("\n You mast be perfect... or a liar :)")
print("\n So, here is all we collect about You:")
print(dict_baseinfo)




