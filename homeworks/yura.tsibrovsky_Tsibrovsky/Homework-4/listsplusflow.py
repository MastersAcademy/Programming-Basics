#! /usr/bin/env python
# -*- coding: utf-8 -*-
print("\n this program will collect your info and pull it into list :) \n")
print("\n Enter your data, please \n")
# data collection
list_fio = []
name_string = input("Name ")
list_fio.append(name_string)
surname_string = input("Last name ")
list_fio.append(surname_string)
age_integer = int(input("Your age "))
if age_integer >= 100:
	age_group = "highlander :) "
elif age_integer < 0:
	age_group = 'cheater'


for age_integer in range(0,10):
    age_group = 'child'
for age_integer in range(10,20):
    age_group = 'teenager'
for age_integer in range(20,25):
    age_group = 'youth'
for age_integer in range(25,65):
    age_group = 'adult'
for age_integer in range(65,100):
    age_group = 'senior'


list_fio.append(age_group)
dict_baseinfo = {
    'first_name': name_string,
    'last_name': surname_string,
    'age categoty': age_group
}

print(dict_baseinfo)
print('Enter additional data, please \n')
hobby1_string = input("Your main hobby, please ")
hobby2_string = input("Your secondary hobby, please ")
dict_baseinfo['hobbies'] = [hobby1_string, hobby2_string]
print(dict_baseinfo)

print("\nDo you have bad habbits ?")
select_string = input("y/n ")
if select_string == 'y':
    badhabbit1_string = input("bad habbit № 1 ")
    badhabbit2_string = input("bad habbit № 2 ")
    badhabbit3_string = input("bad habbit № 3 ")
    dict_badhabbits = {
        '1:': badhabbit1_string,
        '2:': badhabbit2_string,
        '3:': badhabbit3_string
    }
    dict_baseinfo['bad habbits'] = dict_badhabbits
else:
    print("\n You mast be perfect... or a liar :)")

print("\n So, here is all we collect about You:")
print(dict_baseinfo)
